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


def split_tables(all_tokens, types):
    for token in all_tokens:
        tokens = group_tokens(token.flatten())

        create_token = tokens.token_next_match(0, T.DDL, 'CREATE')
        if create_token is None:
            continue

        create_table_token = tokens.token_next_match(create_token, T.Keyword, 'TABLE')
        if create_table_token is None:
            create_type_token = tokens.token_next_match(create_token, T.Keyword, 'TYPE')
            if create_type_token is not None:
                parse_type(tokens, types)
            continue

        table = tokens.token_next(create_table_token)
        columns = split_columns(tokens.token_next(table).tokens[1:-1])

        yield table.value, columns


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
        if token.value.startswith('--') and 'references' in token.value:
            match = re.search(r'references\s+(\S+)', token.value)
            return match.group(1)
        token = tokens.token_next(token)


def generate_models_from_sql(sql):
    yield '# Automatically generated, do not edit'
    yield ''
    yield 'from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DateTime, Date, Enum, Interval, Float, CHAR'
    yield 'from sqlalchemy.dialects.postgres import ARRAY, UUID, SMALLINT'
    yield 'from sqlalchemy.ext.declarative import declarative_base'
    yield 'from sqlalchemy.orm import relationship'
    yield ''
    yield 'Base = declarative_base()'
    yield ''
    yield ''

    types = {}
    tokens = sqlparse.parse(sql)
    for table_name, columns in split_tables(tokens, types):
        model_name = format_class_name(table_name)
        yield 'class {0}(Base):'.format(model_name)
        yield '    __tablename__ = {0!r}'.format(table_name)
        yield '    __table_args__ = { "schema" : "musicbrainz" }'
        yield ''

        foreign_keys = []
        for column in columns.tokens:
            column_name = column.token_next(-1).value.lower()
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
            elif type_name == 'BOOLEAN':
                column_type = 'Boolean'
            elif type_name == 'INTERVAL':
                column_type = 'Interval'
            elif type_name == 'POINT':
                column_type = 'ARRAY(Float)'
            elif type_name == 'CUBE':
                column_type = 'String' # XXX
            elif type_name in types:
                column_type = 'Enum({0}, name={1!r})'.format(', '.join(('{0!r}'.format(t) for t in types[type_name])), type_name)
            else:
                raise ValueError(' '.join(map(str, column.tokens)))

            params = [column_type]

            foreign_key = parse_foreign_key(column, type)
            if foreign_key:
                if foreign_key.endswith('.id'):
                    params.insert(0, repr(column_name))
                    foreign_keys.append((column_name, foreign_key))
                    column_name += '_id'
                params.append('ForeignKey({0!r})'.format('musicbrainz.' + foreign_key))

            if is_not_null(column, type):
                column_attributes['nullable'] = 'False'

            if is_primary_key(column, type):
                column_attributes['primary_key'] = 'True'

            for name, value in column_attributes.iteritems():
                params.append('{0}={1}'.format(name, value))

            yield '    {0} = Column({1})'.format(column_name, ', '.join(params))

        if foreign_keys:
            yield ''
            for column_name, foreign_key in foreign_keys:
                foreign_table_name, foreign_column_name = foreign_key.split('.')
                foreign_model_name = format_class_name(foreign_table_name)
                yield '    {0} = relationship({1!r}, foreign_keys=[{2}])'.format(column_name, foreign_model_name, column_name + '_id')

        yield ''
        yield ''


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('sql')
    args = parser.parse_args()

    with open(args.sql, 'r') as file:
        sql = file.read()

    for line in generate_models_from_sql(sql):
        print line

