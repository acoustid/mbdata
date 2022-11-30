from __future__ import print_function
import time
import tarfile
import sys
import re
import os
import psycopg2
import argparse
import six
import logging
from io import BytesIO
from urllib.parse import urljoin
from six.moves.urllib.request import urlopen
from six.moves.urllib.error import HTTPError
import tempfile
import shutil
import subprocess
from typing import List, Optional
from six.moves import configparser as ConfigParser
from contextlib import ExitStack

logger = logging.getLogger(__name__)


def str_to_bool(x):
    return x.lower() in ('1', 'on', 'true')


def read_env_item(obj, key, name, convert=None):
    value = None
    if name in os.environ:
        value = os.environ[name]
    if name + '_FILE' in os.environ:
        value = open(os.environ[name + '_FILE']).read().strip()
    if value is not None:
        if convert is not None:
            value = convert(value)
        setattr(obj, key, value)


class DatabaseConfig(object):

    def __init__(self) -> None:
        self.name = 'musicbrainz'
        self.host: Optional[str] = None
        self.port: Optional[int] = None
        self.user: str = 'musicbrainz'
        self.password: Optional[str] = None
        self.admin_user: str = 'postgres'
        self.admin_password: Optional[str] = None

    def create_psycopg2_kwargs(self, superuser=False):
        kwargs = {}
        if superuser:
            kwargs['user'] = self.admin_user
            if self.admin_password is not None:
                kwargs['password'] = self.admin_password
        else:
            kwargs['user'] = self.user
            if self.password is not None:
                kwargs['password'] = self.password
        kwargs['database'] = self.name
        if self.host is not None:
            kwargs['host'] = self.host
        if self.port is not None:
            kwargs['port'] = self.port
        return kwargs

    def create_psql_args(self, superuser=False):
        args = []
        if superuser:
            args.append('-U')
            args.append(self.superuser)
        else:
            args.append('-U')
            args.append(self.user)
        if self.host is not None:
            args.append('-h')
            args.append(self.host)
        if self.port is not None:
            args.append('-p')
            args.append(six.text_type(self.port))
        args.append(self.name)
        return args

    def read(self, parser, section):
        self.name = parser.get(section, 'name')
        if parser.has_option(section, 'host'):
            self.host = parser.get(section, 'host')
        if parser.has_option(section, 'port'):
            self.port = parser.getint(section, 'port')
        if parser.has_option(section, 'user'):
            self.user = parser.get(section, 'user')
        if parser.has_option(section, 'password'):
            self.password = parser.get(section, 'password')
        if parser.has_option(section, 'admin_user'):
            self.admin_user = parser.get(section, 'admin_user')
        if parser.has_option(section, 'admin_password'):
            self.admin_password = parser.get(section, 'admin_password')

    def read_env(self, prefix):
        read_env_item(self, 'name', prefix + 'DB_DB')
        read_env_item(self, 'host', prefix + 'DB_HOST')
        read_env_item(self, 'port', prefix + 'DB_PORT', convert=int)
        read_env_item(self, 'user', prefix + 'DB_USER')
        read_env_item(self, 'password', prefix + 'DB_PASSWORD')
        read_env_item(self, 'admin_user', prefix + 'DB_ADMIN_USER')
        read_env_item(self, 'admin_password', prefix + 'DB_ADMIN_PASSWORD')


class SchemasConfig(object):

    def __init__(self):
        self.mapping = {}
        self.ignored_schemas = set()

    def name(self, name):
        return self.mapping.get(name, name)

    def read(self, parser, section):
        for name, value in parser.items(section):
            if name == 'ignore':
                self.ignored_schemas = set([s.strip() for s in value.split(',')])
            else:
                self.mapping[name] = value

    def read_env(self, prefix):
        pass


class TablesConfig(object):

    def __init__(self):
        self.ignored_tables = set()

    def read(self, parser, section):
        for name, value in parser.items(section):
            if name == 'ignore':
                self.ignored_tables = set([s.strip() for s in value.split(',')])

    def read_env(self, prefix):
        pass


class MusicBrainzConfig(object):

    def __init__(self):
        self.base_url = 'https://metabrainz.org/api/musicbrainz/'
        self.token = ''

    def read(self, parser, section):
        if parser.has_option(section, 'base_url'):
            self.base_url = parser.get(section, 'base_url')
        if parser.has_option(section, 'token'):
            self.token = parser.get(section, 'token')

    def read_env(self, prefix):
        read_env_item(self, 'base_url', prefix + 'MUSICBRAINZ_BASE_URL')
        read_env_item(self, 'token', prefix + 'MUSICBRAINZ_TOKEN')


class Config(object):

    def __init__(self, paths):
        self.cfg = ConfigParser.RawConfigParser()
        for path in paths:
            if os.path.exists(path):
                self.cfg.read(path)
        self.get = self.cfg.get
        self.has_option = self.cfg.has_option

        self.database = DatabaseConfig()
        self.musicbrainz = MusicBrainzConfig()
        self.tables = TablesConfig()
        self.schemas = SchemasConfig()

        if self.cfg.has_section('database'):
            self.database.read(self.cfg, 'database')
        elif self.cfg.has_section('DATABASE'):
            self.database.read(self.cfg, 'DATABASE')

        if self.cfg.has_section('musicbrainz'):
            self.musicbrainz.read(self.cfg, 'musicbrainz')
        elif self.cfg.has_section('MUSICBRAINZ'):
            self.musicbrainz.read(self.cfg, 'MUSICBRAINZ')

        if self.cfg.has_section('tables'):
            self.tables.read(self.cfg, 'tables')
        elif self.cfg.has_section('TABLES'):
            self.tables.read(self.cfg, 'TABLES')

        if self.cfg.has_section('schemas'):
            self.schemas.read(self.cfg, 'schemas')

        self.database.read_env('MBSLAVE_')
        self.musicbrainz.read_env('MBSLAVE_')
        self.tables.read_env('MBSLAVE_')
        self.schemas.read_env('MBSLAVE_')

    def connect_db(self, set_search_path=False, superuser=False):
        db = psycopg2.connect(**self.database.create_psycopg2_kwargs(superuser=superuser))
        if set_search_path:
            db.cursor().execute("SET search_path TO %s", (self.schemas.name('musicbrainz'),))
        return db


def connect_db(cfg, set_search_path=False, superuser=False):
    return cfg.connect_db(set_search_path=set_search_path, superuser=superuser)


def parse_name(config, table):
    if '.' in table:
        schema, table = table.split('.', 1)
    else:
        schema = 'musicbrainz'
    schema = config.schemas.name(schema.strip('"'))
    table = table.strip('"')
    return schema, table


def fqn(schema, table):
    return '%s.%s' % (schema, table)


def check_table_exists(db, schema, table):
    cursor = db.cursor()
    cursor.execute("SELECT 1 FROM pg_tables WHERE schemaname=%s AND tablename=%s", (schema, table))
    if not cursor.fetchone():
        return False
    return True


def load_tar(source: str, fileobj: BytesIO, db, config, ignored_schemas, ignored_tables):
    logger.info("Importing data from %s", source)
    tar = tarfile.open(fileobj=fileobj, mode='r|*')
    cursor = db.cursor()
    for member in tar:
        if not member.name.startswith('mbdump/'):
            continue
        name = member.name.split('/')[1].replace('_sanitised', '')
        schema, table = parse_name(config, name)
        fulltable = fqn(schema, table)
        if schema in ignored_schemas:
            logger.info("Ignoring %s", name)
            continue
        if table in ignored_tables:
            logger.info("Ignoring %s", name)
            continue
        if not check_table_exists(db, schema, table):
            logger.info("Skipping %s (table %s does not exist)", name, fulltable)
            continue
        cursor.execute("SELECT 1 FROM %s LIMIT 1" % fulltable)
        if cursor.fetchone():
            logger.info("Skipping %s (table %s already contains data)", name, fulltable)
            continue
        logger.info("Loading %s to %s", name, fulltable)
        cursor.copy_expert('COPY {} FROM STDIN'.format(fulltable), tar.extractfile(member))
        db.commit()


def mbslave_import_main(config, args):
    db = config.database.connect_db(superuser=True, set_search_path=False)


    for source in args.sources:
        with ExitStack() as exit_stack:
            if source.startswith('http://') or source.startswith('https://'):
                fileobj = exit_stack.enter_context(urlopen(source))
            else:
                fileobj = exit_stack.enter_context(open(source, 'rb'))
            load_tar(source, fileobj, db, config, config.schemas.ignored_schemas, config.tables.ignored_tables)


def mbslave_auto_import_main(config: Config, args) -> None:
    base_url = args.base_url
    if not base_url:
        logger.error("No base URL specified")
        raise SystemExit(1)

    with urlopen(urljoin(base_url, 'LATEST')) as f:
        latest = f.read().decode('utf-8').strip()

    logger.info("Latest dump is %s", latest)

    db = connect_db(config)

    files = [
        'mbdump.tar.bz2',
        'mbdump-derived.tar.bz2',
        'mbdump-cover-art-archive.tar.bz2',
        'mbdump-event-art-archive.tar.bz2',
        'mbdump-stats.tar.bz2',
    ]
    for file in files:
        url = urljoin(base_url, latest + '/' + file)
        with urlopen(url) as fileobj:
            load_tar(url, fileobj, db, config, config.schemas.ignored_schemas, config.tables.ignored_tables)


class ReplicationHook(object):

    def __init__(self, cfg, db, schema):
        self.cfg = cfg
        self.db = db
        self.schema = schema

    def begin(self, seq):
        pass

    def before_commit(self):
        pass

    def after_commit(self):
        pass

    def before_delete(self, table, keys):
        pass

    def before_update(self, table, keys, values):
        pass

    def before_insert(self, table, values):
        pass

    def after_delete(self, table, keys):
        pass

    def after_update(self, table, keys, values):
        pass

    def after_insert(self, table, values):
        pass


def parse_data_fields(s):
    fields = {}
    for name, value in re.findall(r'''"([^"]+)"=('(?:''|[^'])*')? ''', s):
        if not value:
            value = None
        else:
            value = value[1:-1].replace("''", "'").replace("\\\\", "\\")
        fields[name] = value
    return fields


def parse_bool(s):
    return s == 't'


ESCAPES = (('\\b', '\b'), ('\\f', '\f'), ('\\n', '\n'), ('\\r', '\r'),
           ('\\t', '\t'), ('\\v', '\v'), ('\\\\', '\\'))


def unescape(s):
    if s == '\\N':
        return None
    for orig, repl in ESCAPES:
        s = s.replace(orig, repl)
    return s


def read_psql_dump(fp, types):
    for line in fp:
        line = line.decode('utf8')
        values = list(map(unescape, line.rstrip('\r\n').split('\t')))
        for i, value in enumerate(values):
            if value is not None:
                values[i] = types[i](value)
        yield values


class PacketImporter(object):

    def __init__(self, db, config, ignored_schemas, ignored_tables, replication_seq, hook):
        self._db = db
        self._data = {}
        self._transactions = {}
        self._config = config
        self._ignored_schemas = ignored_schemas
        self._ignored_tables = ignored_tables
        self._hook = hook
        self._replication_seq = replication_seq

    def load_pending_data(self, fp):
        dump = read_psql_dump(fp, [int, parse_bool, parse_data_fields])
        for id, key, values in dump:
            self._data[(id, key)] = values

    def load_pending(self, fp):
        dump = read_psql_dump(fp, [int, six.text_type, six.text_type, int])
        for id, table, type, xid in dump:
            schema, table = parse_name(self._config, table)
            transaction = self._transactions.setdefault(xid, [])
            transaction.append((id, schema, table, type))

    def process(self):
        cursor = self._db.cursor()
        stats = {}
        self._hook.begin(self._replication_seq)
        for xid in sorted(self._transactions.keys()):
            transaction = self._transactions[xid]
            # print ' - Running transaction', xid
            # print 'BEGIN; --', xid
            for id, schema, table, type in sorted(transaction):
                if schema == '<ignore>':
                    continue
                if schema in self._ignored_schemas:
                    continue
                if table in self._ignored_tables:
                    continue
                fulltable = fqn(schema, table)
                if fulltable not in stats:
                    stats[fulltable] = {'d': 0, 'u': 0, 'i': 0}
                stats[fulltable][type] += 1
                keys = self._data.get((id, True), {})
                values = self._data.get((id, False), {})
                if type == 'd':
                    sql = 'DELETE FROM %s' % (fulltable,)
                    params = []
                    self._hook.before_delete(table, keys)
                elif type == 'u':
                    sql_values = ', '.join('%s=%%s' % i for i in values)
                    sql = 'UPDATE %s SET %s' % (fulltable, sql_values)
                    params = list(values.values())
                    self._hook.before_update(table, keys, values)
                elif type == 'i':
                    sql_columns = ', '.join(values.keys())
                    sql_values = ', '.join(['%s'] * len(values))
                    sql = 'INSERT INTO %s (%s) VALUES (%s)' % (fulltable, sql_columns, sql_values)
                    params = list(values.values())
                    self._hook.before_insert(table, values)
                if type == 'd' or type == 'u':
                    sql += ' WHERE ' + ' AND '.join('%s%s%%s' % (i, ' IS ' if keys[i] is None else '=') for i in keys.keys())
                    params.extend(keys.values())
                # print sql, params
                cursor.execute(sql, params)
                if type == 'd':
                    self._hook.after_delete(table, keys)
                elif type == 'u':
                    self._hook.after_update(table, keys, values)
                elif type == 'i':
                    self._hook.after_insert(table, values)
            # print 'COMMIT; --', xid
        logger.info('Statistics:')
        for table in sorted(stats.keys()):
            logger.info('   * %-30s\t%d\t%d\t%d' % (table, stats[table]['i'], stats[table]['u'], stats[table]['d']))
        self._hook.before_commit()
        self._db.commit()
        self._hook.after_commit()


class MismatchedSchemaError(Exception):
    pass


def process_tar(fileobj, db, schema, ignored_schemas, ignored_tables, expected_schema_seq, replication_seq, hook):
    logger.info("Processing %s", fileobj.name)
    tar = tarfile.open(fileobj=fileobj, mode='r|*')
    importer = PacketImporter(db, schema, ignored_schemas, ignored_tables, replication_seq, hook)
    for member in tar:
        if member.name == 'SCHEMA_SEQUENCE':
            schema_seq = int(tar.extractfile(member).read().strip())
            if schema_seq != expected_schema_seq:
                raise MismatchedSchemaError("Mismatched schema sequence, %d (database) vs %d (replication packet)" % (expected_schema_seq, schema_seq))
        elif member.name == 'TIMESTAMP':
            ts = tar.extractfile(member).read().strip().decode('utf8')
            logger.info('Packet was produced at %s', ts)
        elif member.name in ('mbdump/Pending', 'mbdump/dbmirror_pending'):
            importer.load_pending(tar.extractfile(member))
        elif member.name in ('mbdump/PendingData', 'mbdump/dbmirror_pendingdata'):
            importer.load_pending_data(tar.extractfile(member))
    importer.process()


def get_packet_url(base_url, token, replication_seq):
    url = base_url.rstrip("/") + "/replication-%d.tar.bz2" % replication_seq
    if token:
        url += '?token=' + token
    return url


def download_packet(base_url, token, replication_seq):
    url = base_url.rstrip("/") + "/replication-%d.tar.bz2" % replication_seq
    if token:
        url += '?token=' + token
    url = get_packet_url(base_url, token, replication_seq)
    clean_url = get_packet_url(base_url, '***', replication_seq)
    logger.info('Downloading %s', clean_url)
    try:
        data = urlopen(url, timeout=60)
    except HTTPError as e:
        if e.code == 404:
            return None
        raise
    tmp = tempfile.NamedTemporaryFile(suffix='.tar.bz2')
    shutil.copyfileobj(data, tmp)
    data.close()
    tmp.seek(0)
    return tmp


def mbslave_sync_main(config, args):
    db = connect_db(config)

    base_url = config.musicbrainz.base_url
    token = config.musicbrainz.token
    ignored_schemas = config.schemas.ignored_schemas
    ignored_tables = config.tables.ignored_tables

    hook_class = ReplicationHook

    while True:
        cursor = db.cursor()
        cursor.execute("SELECT current_schema_sequence, current_replication_sequence FROM %s.replication_control" % config.schemas.name('musicbrainz'))
        schema_seq, replication_seq = cursor.fetchone()
        replication_seq += 1
        hook = hook_class(config, db, config)
        tmp = download_packet(base_url, token, replication_seq)
        if tmp is None:
            logger.info('Not found, stopping')
            if not args.keep_running:
                break
            replication_seq -= 1
            time.sleep(60 * 10)
        else:
            try:
                process_tar(tmp, db, config, ignored_schemas, ignored_tables, schema_seq, replication_seq, hook)
            except MismatchedSchemaError:
                if not args.keep_running:
                    raise
                logger.exception('Schema mismatch')
                replication_seq -= 1
                time.sleep(60 * 10)
            tmp.close()
        sys.stdout.flush()
        sys.stderr.flush()


def remap_schema(config, lines):
    def update_search_path(m):
        schemas = m.group(2).replace("'", '').split(',')
        schemas = [config.schemas.name(s.strip()) for s in schemas]
        return m.group(1) + ', '.join(schemas) + ';'

    def update_schema(m):
        return m.group(1) + config.schemas.name(m.group(2)) + m.group(3)

    for line in lines:
        line = re.sub(r'(SET search_path = )(.+?);', update_search_path, line)
        line = re.sub(r'(\b)(\w+)(\.)', update_schema, line)
        line = re.sub(r'( SCHEMA )(\w+)(;)', update_schema, line)
        yield line


def locate_sql_file(rel_path):
    return os.path.join(os.path.dirname(__file__), 'sql', rel_path)


def mbslave_remap_schema_main(config, args):
    for line in remap_schema(config, sys.stdin):
        sys.stdout.write(line)


def mbslave_print_sql_main(config, args):
    for path in args.files:
        for line in remap_schema(config, open(locate_sql_file(path))):
            sys.stdout.write(line)


def join_lines(lines: List[str]) -> str:
    if not lines:
        return ''
    return '\n'.join(lines) + '\n'


def create_database(config: Config) -> None:
    db = connect_db(config, superuser=True)
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE {config.database.name} WITH OWNER {config.database.user}")
    cursor.execute(f"ALTER DATABASE {config.database.name} SET timezone TO 'UTC'")
    db.commit()


def run_script(script: str


def run_sql_script(name: str, superuser: bool = False) -> None:
    subprocess.run(['bash', '-euxc', f'mbsave psql -f {name}'], check=True)


def create_relations(config: Config) -> None:
    run_sql_script('Extensions.sql', superuser=True)
    run_sql_script('CreateCollations.sql')
    run_sql_script('CreateTypes.sql')
    run_sql_script('CreateTables.sql')
    run_sql_script('caa/CreateTables.sql')
    run_sql_script('eaa/CreateTables.sql')
    run_sql_script('statistics/CreateTables.sql')




def mbslave_init_main(config, args):
    if args.create_database:
        create_database(config)
    
    script = ['CREATE DATABASE {config.database} | mbslave psql -S -a']
    subprocess.run(['bash', '-euxc', join_lines(script)], check=True)



def mbslave_create_schemas_main(config, args):
    script = ['mbslave print-create-schemas-sql | mbslave psql -S']
    subprocess.run(['bash', '-euxc', join_lines(script)], check=True)


def mbslave_create_tables_main(config, args):
    sql_files = [
        ('musicbrainz', 'CreateCollations.sql'),
        ('musicbrainz', 'CreateTypes.sql'),
        ('musicbrainz', 'CreateTables.sql'),
        ('musicbrainz', 'CreateFunctions.sql'),
        ('cover_art_archive', 'caa/CreateTables.sql'),
        ('event_art_archive', 'eaa/CreateTables.sql'),
        ('statistics', 'statistics/CreateTables.sql'),
        ('documenation', 'documenation/CreateTables.sql'),
        ('wikidocs', 'wikidocs/CreateTables.sql'),
    ]
    script = []
    for schema, sql_file in sql_files:
        if schema not in config.schemas.ignored_schemas:
            script.append(f'mbslave psql -f {sql_file}')
    subprocess.run(['bash', '-euxc', join_lines(script)], check=True)


def mbslave_create_primary_keys_main(config, args):
    sql_files = [
        ('musicbrainz', 'CreatePrimaryKeys.sql'),
        ('cover_art_archive', 'caa/CreatePrimaryKeys.sql'),
        ('event_art_archive', 'eaa/CreatePrimaryKeys.sql'),
        ('statistics', 'statistics/CreatePrimaryKeys.sql'),
        ('documenation', 'documenation/CreatePrimaryKeys.sql'),
        ('wikidocs', 'wikidocs/CreatePrimaryKeys.sql'),
    ]
    script = []
    for schema, sql_file in sql_files:
        if schema not in config.schemas.ignored_schemas:
            script.append(f'mbslave psql -f {sql_file}')
    subprocess.run(['bash', '-euxc', join_lines(script)], check=True)


def mbslave_create_indexes_main(config, args):
    sql_files = [
        ('musicbrainz', 'CreateIndexes.sql'),
        ('cover_art_archive', 'caa/CreateIndexes.sql'),
        ('event_art_archive', 'eaa/CreateIndexes.sql'),
        ('statistics', 'statistics/CreateIndexes.sql'),
    ]
    script = []
    for schema, sql_file in sql_files:
        if schema not in config.schemas.ignored_schemas:
            script.append(f'mbslave psql -f {sql_file}')
    subprocess.run(['bash', '-euxc', join_lines(script)], check=True)


def mbslave_print_create_schemas_sql_main(config, args):
    all_schemas = [
        'musicbrainz',
        'cover_art_archive',
        'event_art_archive',
        'documentation',
        'statistics',
        'wikidocs'
    ]

    for schema in all_schemas:
        if schema not in config.schemas.ignored_schemas:
            name = config.schemas.name(schema)
            print("CREATE SCHEMA IF NOT EXISTS %s;" % name)


def mbslave_psql_main(config, args):
    command = ['psql'] + config.database.create_psql_args(superuser=args.superuser)

    environ = os.environ.copy()
    if not args.public:
        schema = config.schemas.name(args.schema)
        environ['PGOPTIONS'] = '-c search_path=%s,public' % schema

    if args.superuser:
        if config.database.admin_password:
            environ['PGPASSWORD'] = config.database.admin_password
    else:
        if config.database.password:
            environ['PGPASSWORD'] = config.database.password

    with ExitStack() as es:
        if args.sql_file:
            sql_file = es.enter_context(tempfile.NamedTemporaryFile(suffix='.sql'))
            with open(locate_sql_file(args.sql_file), 'rb') as input_sql_file:
                lines = [line.decode('utf8') for line in input_sql_file]
                for line in remap_schema(config, lines):
                    sql_file.write(line.encode('utf8'))
            sql_file.flush()
            command.insert(-1, '-f')
            command.insert(-1, sql_file.name)

        process = subprocess.Popen(command, env=environ)
        raise SystemExit(process.wait())


def join_paths(paths):
    # type: (List[str]) -> str
    return os.pathsep.join(paths)


def split_paths(s):
    # type: (str) -> List[str]
    return [p.strip() for p in s.split(os.pathsep)]


def main():
    default_config_paths = ['mbslave.conf', '/etc/mbslave.conf']
    if 'MBSLAVE_CONFIG' in os.environ:
        default_config_paths = [os.environ['MBSLAVE_CONFIG']]

    default_config_path = os.pathsep.join(default_config_paths)

    parser = argparse.ArgumentParser()
    parser.add_argument('-c, --config', dest='config_path', metavar='PATH',
                        default=default_config_path,
                        help='path to the config file (default: {})'.format(default_config_path))

    subparsers = parser.add_subparsers()

    parser_init = subparsers.add_parser('init')
    parser_init.add_argument('--create-database', action='store_true')
    parser_init.add_argument('--empty', action='store_true')
    parser_init.set_defaults(func=mbslave_init_main, create_database=False, empty=False)

    parser_create_schemas = subparsers.add_parser('create-schemas')
    parser_create_schemas.set_defaults(func=mbslave_create_schemas_main)

    parser_create_tables = subparsers.add_parser('create-tables')
    parser_create_tables.set_defaults(func=mbslave_create_tables_main)

    parser_create_primary_keys = subparsers.add_parser('create-primary-keys')
    parser_create_primary_keys.set_defaults(func=mbslave_create_primary_keys_main)

    parser_create_indexes = subparsers.add_parser('create-indexes')
    parser_create_indexes.set_defaults(func=mbslave_create_indexes_main)

    parser_import = subparsers.add_parser('import')
    parser_import.add_argument('sources', metavar='FILE_OR_URL', nargs='+', help='tar.bz2 file to import')
    parser_import.set_defaults(func=mbslave_import_main)

    parser_auto_import = subparsers.add_parser('auto-import')
    parser_auto_import.add_argument(
        '--mirror',
        dest='base_url',
        metavar='URL',
        help='URL of the data dump mirror',
        default='http://ftp.musicbrainz.org/pub/musicbrainz/data/fullexport/',
    )
    parser_auto_import.set_defaults(func=mbslave_auto_import_main)

    parser_sync = subparsers.add_parser('sync')
    parser_sync.add_argument('-r, --keep-running', dest='keep_running', action='store_true',
                             help='keep running until the script is explicitly terminated')
    parser_sync.set_defaults(func=mbslave_sync_main)

    parser_remap_schema = subparsers.add_parser('remap-schema')
    parser_remap_schema.set_defaults(func=mbslave_remap_schema_main)

    parser_print_sql = subparsers.add_parser('print-sql')
    parser_print_sql.add_argument('files', metavar='FILE', nargs='+', help='sql file to print')
    parser_print_sql.set_defaults(func=mbslave_print_sql_main)

    parser_print_create_schemas_sql = subparsers.add_parser('print-create-schemas-sql')
    parser_print_create_schemas_sql.set_defaults(func=mbslave_print_create_schemas_sql_main)

    parser_psql = subparsers.add_parser('psql')
    parser_psql.add_argument('-f, --file', dest='sql_file', metavar='FILE', help='sql file to execute')
    parser_psql.add_argument('-S, --no-schema', dest='public', action='store_true',
                             help="don't configure the default schema")
    parser_psql.add_argument('-s, --schema', dest='schema', default='musicbrainz',
                             help="default schema")
    parser_psql.add_argument('--superuser', dest='superuser', action='store_true',
                             help="connect as superuser")
    parser_psql.set_defaults(func=mbslave_psql_main)

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    config = Config(split_paths(args.config_path))
    args.func(config, args)
