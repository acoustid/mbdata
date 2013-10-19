import re
import sqlparse
from sqlparse import tokens as T
from sqlparse.sql import Function, Parenthesis, TokenList


ACRONYMS = set(['ipi', 'isni', 'gid', 'url', 'iso', 'isrc', 'iswc', 'cdtoc'])


def capitalize(word):
    if word in ACRONYMS:
        return word.upper()
    return word.title()


def format_class_name(table_name):
    words = list(table_name.split('_'))
    if words[0] == 'l':
        words[0] = 'link'
    return ''.join([capitalize(word) for word in words])


def group_tokens(tokens):
    stack = [[]]
    for token in tokens:
        if token.is_whitespace():
            continue
        if token.match(T.Punctuation, '('):
            stack.append([token])
        else:
            stack[-1].append(token)
            if token.match(T.Punctuation, ')'):
                group = stack.pop()
                stack[-1].append(TokenList(group))
    return TokenList(stack[0])


def split_columns(tokens):
    columns = []
    column = []
    end_of_column = False
    for token in tokens:
        if end_of_column and not token.value.startswith('--'):
            columns.append(TokenList(column))
            column = []
            end_of_column = False
        column.append(token)
        if token.match(T.Punctuation, ','):
            end_of_column = True
    if column:
        columns.append(TokenList(column))
    return TokenList(columns)


def parse_type(tokens, types):
    name = tokens.token_next(1).value.upper()
    values = [t.value.strip("'") for t in tokens.token_next(4).tokens if t.ttype == T.String.Single]
    types[name] = values


def parse_search_path(tokens):
    return str(tokens.token_next(2).value.strip("'"))


def split_tables(all_tokens, types):
    schema_name = 'musicbrainz'

    for token in all_tokens:
        tokens = group_tokens(token.flatten())

        create_token = tokens.token_next_match(0, T.DDL, 'CREATE')
        if create_token is None:
            set_token = tokens.token_next_match(0, T.Keyword, 'SET')
            if set_token is not None:
                set_search_path = tokens.token_next_match(0, T.Name, 'search_path')
                if set_search_path is not None:
                    schema_name = parse_search_path(tokens)
            continue

        create_table_token = tokens.token_next_match(create_token, T.Keyword, 'TABLE')
        if create_table_token is None:
            create_type_token = tokens.token_next_match(create_token, T.Keyword, 'TYPE')
            if create_type_token is not None:
                parse_type(tokens, types)
            continue

        table = tokens.token_next(create_table_token)
        columns = split_columns(tokens.token_next(table).tokens[1:-1])

        yield schema_name, str(table.value), columns


def next_tokens_match(tokens, idx, texts):
    token = tokens.token_next(idx)
    for text in texts:
        if token is None:
            return False
        if token.value != text:
            return False
        token = tokens.token_next(token)
    return True


def is_not_null(tokens, idx):
    token = tokens.token_next(idx)
    while token is not None:
        if token.match(T.Keyword, 'NOT NULL'):
            return True
        token = tokens.token_next(token)
    return False


def is_primary_key(tokens, idx):
    token = tokens.token_next(idx)
    while token is not None:
        if token.value.startswith('--') and 'PK' in token.value:
            return True
        token = tokens.token_next(token)
    return False


def parse_foreign_key(tokens, idx):
    token = tokens.token_next(idx)
    while token is not None:
        if token.value.startswith('--') and 'references' in token.value and not 'weakly references' in token.value:
            match = re.search(r'references\s+([a-z0-9_.]+)', token.value)
            return str(match.group(1))
        token = tokens.token_next(token)


def split_foreign_key(foreign_key, schema_name=None):
    parts = foreign_key.split('.')
    if len(parts) == 1:
        return schema_name, parts[0], 'id' # XXX this shouldn't happen, but there are errors in CreateTables.sql
    elif len(parts) == 2:
        return schema_name, parts[0], parts[1]
    elif len(parts) == 3:
        return parts[0], parts[1], parts[2]
    raise ValueError('invalid foreign key {0}'.format(foreign_key))


def join_foreign_key(schema_name, table_name, column_name):
    return '{0}.{1}.{2}'.format(schema_name, table_name, column_name)


def generate_models_header():
    yield '# Automatically generated, do not edit'
    yield ''
    yield 'from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DateTime, Date, Enum, Interval, Float, CHAR'
    yield 'from sqlalchemy.dialects.postgres import ARRAY, UUID, SMALLINT, BIGINT'
    yield 'from sqlalchemy.ext.declarative import declarative_base'
    yield 'from sqlalchemy.orm import relationship, composite'
    yield 'from sqlalchemy.ext.hybrid import hybrid_property'
    yield 'from mbdb.types import PartialDate, Point, Cube'
    yield ''
    yield 'Base = declarative_base()'
    yield ''
    yield ''


def generate_models_from_sql(sql):
    types = {}
    tokens = sqlparse.parse(sql)
    for schema_name, table_name, columns in split_tables(tokens, types):
        model_name = format_class_name(table_name)
        yield 'class {0}(Base):'.format(model_name)
        yield '    __tablename__ = {0!r}'.format(table_name)
        yield '    __table_args__ = {0!r}'.format({'schema': schema_name})
        yield ''

        composites = []
        aliases = []
        foreign_keys = []
        for column in columns.tokens:
            column_name = str(column.token_next(-1).value.lower())
            column_type = None
            column_attributes = {}

            if column_name in ('constraint', 'check'):
                continue

            type = column.token_next(0)
            type_name = type.value.upper()
            if type_name == 'SERIAL':
                column_type = 'Integer'
                column_attributes['primary_key'] = 'True'
            elif type_name == 'INTEGER' or type_name == 'INT':
                column_type = 'Integer'
            elif type_name == 'TEXT':
                column_type = 'String'
            elif type_name == 'VARCHAR':
                size = column.token_next(type)
                if size.is_group() and size.tokens[0].match(T.Punctuation, '('):
                    column_type = 'String({0})'.format(size.tokens[1])
                else:
                    column_type = 'String'
            elif type_name == 'CHAR' or type_name == 'CHARACTER':
                size = column.token_next(type)
                if size.is_group() and size.tokens[0].match(T.Punctuation, '('):
                    column_type = 'CHAR({0})'.format(size.tokens[1])
                else:
                    column_type = 'CHAR'
            elif type_name == 'TIMESTAMP':
                column_type = 'DateTime'
                if next_tokens_match(column, type, ['WITH', 'TIME', 'ZONE']):
                    column_type = 'DateTime(timezone=True)'
            elif type_name == 'TIMESTAMPTZ':
                column_type = 'DateTime(timezone=True)'
            elif type_name == 'DATE':
                column_type = 'Date'
            elif type_name == 'UUID':
                column_type = 'UUID'
            elif type_name == 'SMALLINT':
                column_type = 'SMALLINT'
            elif type_name == 'BIGINT':
                column_type = 'BIGINT'
            elif type_name == 'BOOLEAN':
                column_type = 'Boolean'
            elif type_name == 'INTERVAL':
                column_type = 'Interval'
            elif type_name == 'POINT':
                column_type = 'Point'
            elif type_name == 'CUBE':
                column_type = 'Cube'
            elif type_name in types:
                column_type = 'Enum({0}, name={1!r})'.format(', '.join(('{0!r}'.format(t) for t in types[type_name])), type_name)
            else:
                raise ValueError(' '.join(map(str, column.tokens)))

            if column_name.endswith('date_year'):
                composites.append((
                    column_name.replace('_year', ''),
                    'PartialDate',
                    (column_name,
                     column_name.replace('_year', '_month'),
                     column_name.replace('_year', '_day'))
                ))

            attribute_name = column_name
            params = [column_type]

            if schema_name == 'cover_art_archive' and table_name == 'cover_art_type' and column_name == 'type_id':
                attribute_name = 'type'

            foreign_key = parse_foreign_key(column, type)
            if foreign_key:
                foreign_schema_name, foreign_table_name, foreign_column_name = split_foreign_key(foreign_key, schema_name)
                if foreign_column_name == 'id':
                    if attribute_name == 'id':
                        if schema_name == 'cover_art_archive' and table_name == 'cover_art_type':
                            relationship_name = 'cover_art'
                        elif schema_name == 'documentation' and table_name.startswith('l_') and table_name.endswith('_example'):
                            relationship_name = 'link'
                        else:
                            relationship_name = foreign_table_name
                    else:
                        relationship_name = attribute_name
                        attribute_name += '_id'
                    params.insert(0, repr(column_name))
                    foreign_keys.append((attribute_name, relationship_name, foreign_key))
                    if table_name.startswith('l_') and column_name in ('entity0', 'entity1'):
                        if table_name == 'l_{0}_{0}'.format(foreign_table_name, foreign_table_name):
                            aliases.append((column_name, foreign_table_name + column_name[-1]))
                            aliases.append((attribute_name, foreign_table_name + column_name[-1] + '_id'))
                        else:
                            aliases.append((column_name, foreign_table_name))
                            aliases.append((attribute_name, foreign_table_name + '_id'))
                params.append('ForeignKey({0!r})'.format(join_foreign_key(foreign_schema_name, foreign_table_name, foreign_column_name)))

            if is_not_null(column, type):
                column_attributes['nullable'] = 'False'

            if is_primary_key(column, type):
                column_attributes['primary_key'] = 'True'

            for name, value in column_attributes.iteritems():
                params.append('{0}={1}'.format(name, value))

            yield '    {0} = Column({1})'.format(attribute_name, ', '.join(params))

        if foreign_keys:
            yield ''
            for attribute_name, column_name, foreign_key in foreign_keys:
                foreign_schema_name, foreign_table_name, foreign_column_name = split_foreign_key(foreign_key, schema_name)
                foreign_model_name = format_class_name(foreign_table_name)
                yield '    {0} = relationship({1!r}, foreign_keys=[{2}])'.format(column_name, foreign_model_name, attribute_name)

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
        print line

    for file_name in args.sql:
        with open(file_name, 'r') as file:
            sql = file.read()
        for line in generate_models_from_sql(sql):
            print line

