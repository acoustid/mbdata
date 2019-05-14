# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from __future__ import print_function
import os
import re
import sqlparse
import six
from sqlparse import tokens as T
from sqlparse.sql import TokenList, Parenthesis
from typing import List
from mbdata.utils.sql import CreateTable, CreateType, CreateIndex, Set, parse_statements


ACRONYMS = set(['ipi', 'isni', 'gid', 'url', 'iso', 'isrc', 'iswc', 'cdtoc'])
SPECIAL_NAMES = {'coverart': 'CoverArt'}

TYPE_MAPPING = {
    'SERIAL': 'Integer',
    'INT': 'Integer',
    'INTEGER': 'Integer',
    'TEXT': 'String',
    'VARCHAR': 'String',
    'CHAR': 'CHAR',
    'CHARACTER': 'CHAR',
    'TIMESTAMP': 'DateTime',
    'TIMESTAMPTZ': 'DateTime(timezone=True)',
    'TIMESTAMP WITH TIME ZONE': 'DateTime(timezone=True)',
    'TIME WITHOUT TIME ZONE': 'Time(timezone=False)',
    'DATE': 'Date',
    'UUID': 'UUID',
    'SMALLINT': 'SMALLINT',
    'BIGINT': 'BIGINT',
    'BOOLEAN': 'Boolean',
    'INTERVAL': 'Interval',
    'POINT': 'Point',
    'CUBE': 'Cube',
    'JSONB': 'JSONB',
}


def capitalize(word):
    if word in ACRONYMS:
        return word.upper()
    return SPECIAL_NAMES.get(word, word.title())


def format_model_name(table_name):
    words = list(table_name.split('_'))
    if words[0] == 'l':
        words[0] = 'link'
    return str(''.join([capitalize(word) for word in words]))


class CheckConstraint(object):

    def __init__(self, text, name=None):
        self.text = text
        self.name = name


class ForeignKey(object):

    def __init__(self, schema, table, column, cascade=False):
        self.schema = schema
        self.table = table
        self.column = column
        self.cascade = cascade


class Column(object):

    def __init__(self, name, type, nullable=True, default=None, primary_key=False, foreign_key=None, check_constraint=None):
        self.name = name
        self.type = type
        self.nullable = nullable
        self.default = default
        self.primary_key = primary_key
        self.foreign_key = foreign_key
        self.check_constraint = check_constraint


class Table(object):

    def __init__(self, schema, name, columns):
        self.schema = schema
        self.name = name
        self.columns = columns


class Enum(object):

    def __init__(self, schema, name, labels):
        self.schema = schema
        self.name = name
        self.labels = labels


class Index(object):

    def __init__(self, schema, name, table, columns, unique):
        self.schema = schema
        self.name = name
        self.table = table
        self.columns = columns
        self.unique = unique


def split_fqn(fqn, schema=None):
    parts = fqn.split('.')
    if len(parts) == 1:
        return schema, parts[0], 'id'  # XXX this shouldn't happen, but there are errors in CreateTables.sql
    elif len(parts) == 2:
        return schema, parts[0], parts[1]
    elif len(parts) == 3:
        return parts[0], parts[1], parts[2]
    raise ValueError('invalid name {0}'.format(fqn))


def parse_create_table_column(clause, schema):
    column = Column(clause.get_name(), clause.get_type())

    if clause.is_not_null():
        column.nullable = False

    column.default = clause.get_default_value()

    if column.type == 'SERIAL':
        column.primary_key = True

    for comment in clause.get_comments():
        if re.search(r'\bPK\b', comment):
            column.primary_key = True
        match = re.search(r'\b(?:(weakly)\s+)?references\s+([a-z0-9_.]+)(?:\s(CASCADE))?', comment)
        if match is not None and match.group(1) != 'weakly':
            column.foreign_key = ForeignKey(*split_fqn(match.group(2), schema))
            if match.group(3) == 'CASCADE':
                column.foreign_key.cascade = True

    check = clause.get_check_constraint()
    if check is not None:
        column.check_constraint = CheckConstraint(check.get_body(), check.get_name())

    return column


def parse_create_table(statement, schema):
    table = Table(schema, statement.get_name(), [])
    for column_clause in statement.get_columns():
        table.columns.append(parse_create_table_column(column_clause, schema))
    return table


def parse_create_type(statement, schema):
    return Enum(schema, statement.get_name(), statement.get_enum_labels())


def parse_create_index(statement, schema):
    return Index(schema, statement.get_name(), statement.get_table(), statement.get_columns(), unique=statement.is_unique())


def parse_sql(sql, schema='musicbrainz'):
    tables = []
    types = []
    indexes = []

    statements = parse_statements(sqlparse.parse(sql))
    for statement in statements:
        if isinstance(statement, Set) and statement.get_name() == 'search_path':
            schema = statement.get_value().split(',')[0].strip()

        elif isinstance(statement, CreateTable):
            tables.append(parse_create_table(statement, schema))

        elif isinstance(statement, CreateType):
            types.append(parse_create_type(statement, schema))

        elif isinstance(statement, CreateIndex):
            indexes.append(parse_create_index(statement, schema))

    return tables, types, indexes


def join_foreign_key(*args):
    return '.'.join(map(str, args))


def generate_models_header():
    yield '# Automatically generated, do not edit'
    yield ''
    yield '# pylint: disable=C0103'
    yield '# pylint: disable=C0302'
    yield '# pylint: disable=W0232'
    yield ''
    yield 'from sqlalchemy import Column, Index, Integer, String, Text, ForeignKey, Boolean, DateTime, Time, Date, Enum, Interval, CHAR, CheckConstraint, sql'
    yield 'from sqlalchemy.ext.declarative import declarative_base'
    yield 'from sqlalchemy.ext.hybrid import hybrid_property'
    yield 'from sqlalchemy.orm import relationship, composite, backref'
    yield 'from mbdata.types import PartialDate, Point, Cube as _Cube, regexp, UUID, SMALLINT, BIGINT, JSONB'
    yield 'from typing import Any'
    yield ''
    yield 'import mbdata.config'
    yield 'mbdata.config.freeze()'
    yield ''
    yield 'Base = None  # type: Any'
    yield ''
    yield 'if mbdata.config.Base is not None:'
    yield '    Base = mbdata.config.Base'
    yield 'elif mbdata.config.metadata is not None:'
    yield '    Base = declarative_base(metadata=mbdata.config.metadata)'
    yield 'else:'
    yield '    Base = declarative_base()'
    yield ''
    yield 'if mbdata.config.use_cube:'
    yield '    Cube = _Cube'
    yield 'else:'
    yield '    Cube = Text  # noqa: F811'
    yield ''
    yield ''
    yield 'def apply_schema(name, schema):'
    yield '    schema = mbdata.config.schemas.get(schema, schema)'
    yield '    if schema:'
    yield '        name = "{}.{}".format(schema, name)'
    yield '    return name'
    yield ''
    yield ''


def make_type_mapper(types):
    mapping = dict(TYPE_MAPPING)
    for type in types:
        mapping[type.name.upper()] = 'Enum({0}, name={1!r}, schema=mbdata.config.schemas.get({2!r}, {2!r}))'.format(', '.join(('{0!r}'.format(str(l)) for l in type.labels)), str(type.name.upper()), type.schema)

    def inner(type):
        new_type = mapping.get(type.upper())
        if new_type is not None:
            return new_type
        match = re.match(r'(\w+)\((\d+)\)', type)
        if match is not None:
            name, precision = match.groups()
            new_type = mapping.get(name.upper())
            if new_type is not None:
                return '{0}({1})'.format(new_type, precision)
        raise ValueError('unknown type - ' + type)

    return inner


def convert_expression_to_python(token):
    if not token.is_group:
        if token.value.upper() == 'TRUE':
            return 'sql.true()'
        elif token.value.upper() == 'FALSE':
            return 'sql.false()'
        elif token.ttype == T.Name:
            return 'sql.literal_column({0!r})'.format(str(token.value))
        else:
            return 'sql.text({0!r})'.format(str(token.value))

    if isinstance(token, Parenthesis):
        return '({0})'.format(convert_expression_to_python(TokenList(token.tokens[1:-1])))

    elif len(token.tokens) == 1:
        return convert_expression_to_python(token.tokens[0])

    elif len(token.tokens) == 3 and token.tokens[1].ttype == T.Comparison:
        lhs = convert_expression_to_python(token.tokens[0])
        rhs = convert_expression_to_python(token.tokens[2])
        op = token.tokens[1].value
        if op == '=':
            op = '=='
        return '{0} {1} {2}'.format(lhs, op, rhs)

    elif len(token.tokens) == 3 and token.tokens[1].match(T.Keyword, 'IN') and isinstance(token.tokens[2], Parenthesis):
        lhs = convert_expression_to_python(token.tokens[0])
        rhs = [convert_expression_to_python(t) for t in token.tokens[2].tokens[1:-1] if not t.match(T.Punctuation, ',')]
        return '{0}.in_({1!r})'.format(lhs, tuple(rhs))

    elif len(token.tokens) == 4 and token.tokens[1].match(T.Comparison, '~') and token.tokens[2].match(T.Name, 'E') and token.tokens[3].ttype == T.String.Single:
        lhs = convert_expression_to_python(token.tokens[0])
        pattern = token.tokens[3].value.replace('\\\\', '\\')
        return 'regexp({0}, {1})'.format(lhs, pattern)

    elif len(token.tokens) == 3 and token.tokens[1].match(T.Keyword, 'IS') and token.tokens[2].match(T.Keyword, 'NULL'):
        lhs = convert_expression_to_python(token.tokens[0])
        return '{0} == None'.format(lhs)

    elif len(token.tokens) == 3 and token.tokens[1].match(T.Keyword, 'IS') and token.tokens[2].match(T.Keyword, 'NOT NULL'):
        lhs = convert_expression_to_python(token.tokens[0])
        return '{0} != None'.format(lhs)

    else:
        parts = []
        op = None
        idx = -1

        while True:
            new_idx, op_token = token.token_next_by(m=(T.Keyword, ('AND', 'OR')), idx=idx)
            if op_token is None:
                break
            if op is None:
                op = op_token.normalized
            assert op == op_token.normalized
            new_tokens = token.tokens[idx + 1:new_idx]
            if len(new_tokens) == 1:
                parts.append(convert_expression_to_python(new_tokens[0]))
            else:
                parts.append(convert_expression_to_python(TokenList(new_tokens)))
            idx = new_idx + 1

        if idx == -1:
            raise ValueError('unknown expression - {0}'.format(token))

        new_tokens = token.tokens[idx:]
        if len(new_tokens) == 1:
            parts.append(convert_expression_to_python(new_tokens[0]))
        else:
            parts.append(convert_expression_to_python(TokenList(new_tokens)))

        return 'sql.{0}_({1})'.format(op.lower(), ', '.join(parts))


def generate_models_from_sql(tables, types, indexes):
    map_type = make_type_mapper(types)

    for table in tables:
        if table.name == 'old_editor_name':
            continue

        model_name = format_model_name(table.name)
        yield 'class {0}(Base):'.format(model_name)
        yield '    __tablename__ = {0!r}'.format(str(table.name))
        yield '    __table_args__ = ('
        for index in indexes:
            if index.table == table.name and index.schema == table.schema:
                extra = ['{!r}'.format(str(column)) for column in index.columns]
                if index.unique:
                    extra.append('unique=True')
                extra = ', '.join([repr(str(index.name))] + extra)
                if 'DESC' not in extra and '(' not in extra:  # XXX fix
                    yield '        Index({}),'.format(extra)
        yield '        {{\'schema\': mbdata.config.schemas.get({0!r}, {0!r})}}'.format(str(table.schema))
        yield '    )'
        yield ''

        composites = []
        aliases = []
        foreign_keys = []
        for column in table.columns:
            column_type = map_type(column.type)
            column_attributes = {}

            if column.name.endswith('date_year'):
                composites.append((
                    column.name.replace('_year', ''),
                    'PartialDate',
                    (column.name,
                     column.name.replace('_year', '_month'),
                     column.name.replace('_year', '_day'))
                ))

            attribute_name = column.name
            params = [column_type]

            if table.schema == 'cover_art_archive' and table.name == 'cover_art_type' and column.name == 'type_id':
                attribute_name = 'type'
            if table.schema == 'musicbrainz' and table.name.endswith('_gid_redirect') and column.name == 'new_id':
                attribute_name = 'redirect'

            foreign_key = column.foreign_key
            if foreign_key is not None:
                if foreign_key.column in ('id', 'area'):
                    backref = None
                    if table.schema == 'musicbrainz' and table.name == 'artist_credit_name' and column.name == 'artist_credit':
                        backref = 'artists', 'order_by="ArtistCreditName.position"'
                    if table.schema == 'musicbrainz' and table.name == 'track' and column.name == 'medium':
                        backref = 'tracks', 'order_by="Track.position"'
                    if table.schema == 'musicbrainz' and table.name == 'medium' and column.name == 'release':
                        backref = 'mediums', 'order_by="Medium.position"'
                    if table.schema == 'musicbrainz' and table.name == 'isrc' and column.name == 'recording':
                        backref = 'isrcs'
                    if table.schema == 'musicbrainz' and table.name == 'iswc' and column.name == 'work':
                        backref = 'iswcs'
                    if table.schema == 'musicbrainz' and table.name == 'artist_ipi' and column.name == 'artist':
                        backref = 'ipis'
                    if table.schema == 'musicbrainz' and table.name == 'artist_isni' and column.name == 'artist':
                        backref = 'isnis'
                    if table.schema == 'musicbrainz' and table.name == 'label_ipi' and column.name == 'label':
                        backref = 'ipis'
                    if table.schema == 'musicbrainz' and table.name == 'label_isni' and column.name == 'label':
                        backref = 'isnis'
                    if table.schema == 'musicbrainz' and table.name == 'release_label' and column.name == 'release':
                        backref = 'labels'
                    if table.schema == 'musicbrainz' and table.name == 'release_country' and column.name == 'release':
                        backref = 'country_dates'
                    if table.schema == 'musicbrainz' and table.name == 'release_unknown_country' and column.name == 'release':
                        backref = 'unknown_country_dates'
                    if table.schema == 'musicbrainz' and table.name == 'release_group_secondary_type_join' and column.name == 'release_group':
                        backref = 'secondary_types'
                    if table.schema == 'musicbrainz' and table.name.endswith('_meta') and column.name == 'id':
                        backref = 'meta', 'uselist=False'
                    if table.schema == 'musicbrainz' and table.name.startswith('iso_') and column.name == 'area':
                        backref = table.name + '_codes'
                    if attribute_name == 'id':
                        if table.schema == 'cover_art_archive' and table.name == 'cover_art_type':
                            relationship_name = 'cover_art'
                        elif table.schema == 'documentation' and table.name.startswith('l_') and table.name.endswith('_example'):
                            relationship_name = 'link'
                        else:
                            relationship_name = foreign_key.table
                    else:
                        relationship_name = attribute_name
                        attribute_name += '_id'
                    params.insert(0, repr(str(column.name)))
                    foreign_keys.append((attribute_name, relationship_name, foreign_key, backref, column.nullable))
                    if table.name.startswith('l_') and column.name in ('entity0', 'entity1'):
                        if table.name == 'l_{0}_{0}'.format(foreign_key.table, foreign_key.table):
                            aliases.append((column.name, foreign_key.table + column.name[-1]))
                            aliases.append((attribute_name, foreign_key.table + column.name[-1] + '_id'))
                        else:
                            aliases.append((column.name, foreign_key.table))
                            aliases.append((attribute_name, foreign_key.table + '_id'))
                    if table.name.endswith('_gid_redirect') and column.name == 'new_id':
                        aliases.append((attribute_name, column.name))
                        aliases.append((relationship_name, foreign_key.table))

                foreign_key_name = "{0}_fk_{1}".format(table.name, column.name)[:63]
                foreign_key_params = [
                    "apply_schema({0!r}, {1!r})".format(join_foreign_key(foreign_key.table, foreign_key.column), foreign_key.schema),
                    "name='{0}'".format(foreign_key_name),
                ]
                if foreign_key.cascade:
                    foreign_key_params.append("ondelete='CASCADE'")
                params.append('ForeignKey({0})'.format(', '.join(foreign_key_params)))

            if not column.nullable:
                column_attributes['nullable'] = 'False'

            if column.primary_key:
                column_attributes['primary_key'] = 'True'

            if column.default:
                default = str(column.default.lower())
                if default != "null":
                    if default in ("-1", "0", "1") or (default[0] == "'" and default[-1] == "'"):
                        column_attributes['default'] = default
                    elif default in ("true", "false"):
                        column_attributes['default'] = default.title()
                    if default == "now()":
                        column_attributes['server_default'] = 'sql.func.now()'
                    elif default in ("true", "false"):
                        column_attributes['server_default'] = 'sql.{0}()'.format(default)
                    else:
                        column_attributes['server_default'] = 'sql.text({0!r})'.format(default)

            # if column.check_constraint:
            #    check = column.check_constraint
            #    text = convert_expression_to_python(check.text)
            #    if check.name:
            #        params.append('CheckConstraint({0}, name={1!r})'.format(str(text), str(check.name)))
            #    else:
            #        params.append('CheckConstraint({0})'.format(str(text)))

            for name, value in column_attributes.iteritems():
                params.append('{0}={1}'.format(name, value))

            yield '    {0} = Column({1})'.format(attribute_name, ', '.join(params))

        if foreign_keys:
            yield ''
            for attribute_name, relationship_name, foreign_key, backref, nullable in foreign_keys:
                foreign_model_name = format_model_name(foreign_key.table)
                relationship_params = [
                    repr(foreign_model_name),
                    'foreign_keys=[{0}]'.format(attribute_name)
                ]
                if not nullable:
                    relationship_params.append('innerjoin=True')
                if backref:
                    if isinstance(backref, six.string_types):
                        relationship_params.append('backref=backref({0!r})'.format(backref))
                    else:
                        relationship_params.append('backref=backref({0!r}, {1})'.format(backref[0], ', '.join(backref[1:])))
                yield '    {0} = relationship({1})'.format(relationship_name, ', '.join(relationship_params))

        for old_name, new_name in aliases:
            yield ''
            yield '    @hybrid_property'
            yield '    def {0}(self):'.format(new_name)
            yield '        return self.{0}'.format(old_name)

        if composites:
            yield ''
            for name, type, columns in composites:
                yield '    {0} = composite({1}, {2})'.format(name, type, ', '.join(columns))

        yield ''
        yield ''


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('sql', nargs='+')
    args = parser.parse_args()

    for line in generate_models_header():
        print(line)

    tables = []  # type: List[CreateTable]
    types = []  # type: List[CreateType]
    indexes = []  # type: List[CreateIndex]
    for file_name in args.sql:
        file_names = [file_name]

        indexes_file_name = file_name.replace('CreateTables', 'CreateIndexes')
        if os.path.exists(indexes_file_name):
            file_names.append(indexes_file_name)

        for file_name in file_names:
            with open(file_name, 'r') as file:
                sql = file.read()
                tables2, types2, indexes2 = parse_sql(sql)
                tables.extend(tables2)
                types.extend(types2)
                indexes.extend(indexes2)

    for line in generate_models_from_sql(tables, types, indexes):
        print(line)

