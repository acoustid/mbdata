import time
import tarfile
import sys
import re
import os
import psycopg2
import argparse
import urllib2
import tempfile
import shutil
import ConfigParser


class ConfigSection(object):
    pass


class SchemasConfig(object):

    def __init__(self):
        self.mapping = {}

    def name(self, name):
        return self.mapping.get(name, name)

    def parse(self, parser, section):
        for name, value in parser.items(section):
            self.mapping[name] = value


class Config(object):

    def __init__(self, path):
        self.path = path
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(self.path)
        self.get = self.cfg.get
        self.has_option = self.cfg.has_option
        self.database = ConfigSection()
        self.schema = SchemasConfig()
        if self.cfg.has_section('schemas'):
            self.schema.parse(self.cfg, 'schemas')

    def make_psql_args(self):
        opts = {}
        opts['database'] = self.cfg.get('DATABASE', 'name')
        opts['user'] = self.cfg.get('DATABASE', 'user')
        if self.cfg.has_option('DATABASE', 'password'):
            opts['password'] = self.cfg.get('DATABASE', 'password')
        if self.cfg.has_option('DATABASE', 'host'):
            opts['host'] = self.cfg.get('DATABASE', 'host')
        if self.cfg.has_option('DATABASE', 'port'):
            opts['port'] = self.cfg.get('DATABASE', 'port')
        return opts


def connect_db(cfg, set_search_path=False):
    db = psycopg2.connect(**cfg.make_psql_args())
    if set_search_path:
        db.cursor().execute("SET search_path TO %s", (cfg.schema.name('musicbrainz'),))
    return db


def parse_name(config, table):
    if '.' in table:
        schema, table = table.split('.', 1)
    else:
        schema = 'musicbrainz'
    schema = config.schema.name(schema.strip('"'))
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


def load_tar(filename, db, config, ignored_schemas, ignored_tables):
    print "Importing data from", filename
    tar = tarfile.open(filename, 'r:bz2')
    cursor = db.cursor()
    for member in tar:
        if not member.name.startswith('mbdump/'):
            continue
        name = member.name.split('/')[1].replace('_sanitised', '')
        schema, table = parse_name(config, name)
        fulltable = fqn(schema, table)
        if schema in ignored_schemas:
            print " - Ignoring", name
            continue
        if table in ignored_tables:
            print " - Ignoring", name
            continue
        if not check_table_exists(db, schema, table):
            print " - Skipping %s (table %s does not exist)" % (name, fulltable)
            continue
        cursor.execute("SELECT 1 FROM %s LIMIT 1" % fulltable)
        if cursor.fetchone():
            print " - Skipping %s (table %s already contains data)" % (name, fulltable)
            continue
        print " - Loading %s to %s" % (name, fulltable)
        cursor.copy_from(tar.extractfile(member), fulltable)
        db.commit


def mbslave_import_main(config, args):
    db = connect_db(config)

    ignored_schemas = set(config.get('schemas', 'ignore').split(','))
    ignored_tables = set(config.get('TABLES', 'ignore').split(','))
    for filename in args.files:
        load_tar(filename, db, config, ignored_schemas, ignored_tables)


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
        values = map(unescape, line.rstrip('\r\n').split('\t'))
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
        dump = read_psql_dump(fp, [int, str, str, int])
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
                    params = values.values()
                    self._hook.before_update(table, keys, values)
                elif type == 'i':
                    sql_columns = ', '.join(values.keys())
                    sql_values = ', '.join(['%s'] * len(values))
                    sql = 'INSERT INTO %s (%s) VALUES (%s)' % (fulltable, sql_columns, sql_values)
                    params = values.values()
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
        print ' - Statistics:'
        for table in sorted(stats.keys()):
            print '   * %-30s\t%d\t%d\t%d' % (table, stats[table]['i'], stats[table]['u'], stats[table]['d'])
        self._hook.before_commit()
        self._db.commit()
        self._hook.after_commit()


def process_tar(fileobj, db, schema, ignored_schemas, ignored_tables, expected_schema_seq, replication_seq, hook):
    print "Processing", fileobj.name
    tar = tarfile.open(fileobj=fileobj, mode='r:bz2')
    importer = PacketImporter(db, schema, ignored_schemas, ignored_tables, replication_seq, hook)
    for member in tar:
        if member.name == 'SCHEMA_SEQUENCE':
            schema_seq = int(tar.extractfile(member).read().strip())
            if schema_seq != expected_schema_seq:
                raise Exception("Mismatched schema sequence, %d (database) vs %d (replication packet)" % (expected_schema_seq, schema_seq))
        elif member.name == 'TIMESTAMP':
            ts = tar.extractfile(member).read().strip()
            print ' - Packet was produced at', ts
        elif member.name in ('mbdump/Pending', 'mbdump/dbmirror_pending'):
            importer.load_pending(tar.extractfile(member))
        elif member.name in ('mbdump/PendingData', 'mbdump/dbmirror_pendingdata'):
            importer.load_pending_data(tar.extractfile(member))
    importer.process()


def download_packet(base_url, token, replication_seq):
    url = base_url.rstrip("/") + "/replication-%d.tar.bz2" % replication_seq
    if token:
        url += '?token=' + token
    print "Downloading", url
    try:
        data = urllib2.urlopen(url, timeout=60)
    except urllib2.HTTPError, e:
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

    base_url = config.get('MUSICBRAINZ', 'base_url')
    if config.has_option('MUSICBRAINZ', 'token'):
        token = config.get('MUSICBRAINZ', 'token')
    else:
        token = None
    ignored_schemas = set(config.get('schemas', 'ignore').split(','))
    ignored_tables = set(config.get('TABLES', 'ignore').split(','))

    hook_class = ReplicationHook

    cursor = db.cursor()
    cursor.execute("SELECT current_schema_sequence, current_replication_sequence FROM %s.replication_control" % config.schema.name('musicbrainz'))
    schema_seq, replication_seq = cursor.fetchone()

    while True:
        replication_seq += 1
        hook = hook_class(config, db, config)
        tmp = download_packet(base_url, token, replication_seq)
        if tmp is None:
            print 'Not found, stopping'
            if not args.keep_running:
                break
            replication_seq -= 1
            time.sleep(60 * 10)
        else:
            process_tar(tmp, db, config, ignored_schemas, ignored_tables, schema_seq, replication_seq, hook)
            tmp.close()


def mbslave_remap_schema_main(config, args):
    def update_search_path(m):
        schemas = m.group(2).replace("'", '').split(',')
        schemas = [config.schema.name(s.strip()) for s in schemas]
        return m.group(1) + ', '.join(schemas) + ';'

    def update_schema(m):
        return m.group(1) + config.schema.name(m.group(2)) + m.group(3)

    for line in sys.stdin:
        line = re.sub(r'(SET search_path = )(.+?);', update_search_path, line)
        line = re.sub(r'(\b)(\w+)(\.)', update_schema, line)
        line = re.sub(r'( SCHEMA )(\w+)(;)', update_schema, line)
        sys.stdout.write(line)


def mbslave_psql_main(config, args):
    args = ['psql']
    args.append('-U')
    args.append(config.get('DATABASE', 'user'))
    if config.has_option('DATABASE', 'host'):
        args.append('-h')
        args.append(config.get('DATABASE', 'host'))
    if config.has_option('DATABASE', 'port'):
        args.append('-p')
        args.append(config.get('DATABASE', 'port'))
    args.append(config.get('DATABASE', 'name'))

    if not args.public:
        schema = config.schema.name(args.schema)
        os.environ['PGOPTIONS'] = '-c search_path=%s,public' % schema
    if config.has_option('DATABASE', 'password'):
        os.environ['PGPASSWORD'] = config.get('DATABASE', 'password')
    os.execvp("psql", args)


def main():
    default_config_path = 'mbslave.conf'
    if 'MBSLAVE_CONFIG' in os.environ:
        default_config_path = os.environ['MBSLAVE_CONFIG']

    parser = argparse.ArgumentParser()
    parser.add_argument('-c, --config', dest='config_path', metavar='PATH',
                        default=default_config_path,
                        help='path to the config file (default: {})'.format(default_config_path))

    subparsers = parser.add_subparsers()

    parser_import = subparsers.add_parser('import')
    parser_import.add_argument('files', metavar='FILE', nargs='+', help='tar.bz2 file to import')
    parser_import.set_defaults(func=mbslave_import_main)

    parser_sync = subparsers.add_parser('sync')
    parser_sync.add_argument('-r, --keep-running', dest='keep_running', action='store_true',
                             help='keep running until the script is explicitly terminated')
    parser_sync.set_defaults(func=mbslave_sync_main)

    parser_remap_schema = subparsers.add_parser('remap-schema')
    parser_remap_schema.set_defaults(func=mbslave_remap_schema_main)

    parser_psql = subparsers.add_parser('psql')
    parser_psql.add_argument('-S, --no-schema', dest='public', action='store_true',
                             help="don't configure the default schema")
    parser_psql.add_argument('-s, --schema', dest='schema', default='musicbrainz',
                             help="default schema")
    parser_psql.set_defaults(func=mbslave_psql_main)

    args = parser.parse_args()

    config = Config(args.config_path)
    args.func(config, args)
