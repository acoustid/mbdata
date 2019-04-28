from __future__ import print_function
import sys
from nose.tools import assert_equal, assert_true, assert_false, assert_is_instance, assert_multi_line_equal
from six import StringIO
import sqlparse
from sqlparse import tokens as T
from sqlparse.sql import Token, TokenList, Parenthesis
from mbdata.utils.sql import (
    group_parentheses,
    parse_statements,
    Set,
    CreateTable,
    CreateType,
    CreateIndex,
)


def test_group_parentheses():
    tokens = [
        Token(T.Keyword, 'CREATE'),
        Token(T.Whitespace, ' '),
        Token(T.Keyword, 'TABLE'),
        Token(T.Whitespace, ' '),
        Token(T.Name, 'table_name'),
        Token(T.Whitespace, ' '),
        Token(T.Punctuation, '('),
        Token(T.Name, 'id'),
        Token(T.Whitespace, ' '),
        Token(T.Keyword, 'SERIAL'),
        Token(T.Whitespace, ' '),
        Token(T.Keyword, 'CHECK'),
        Token(T.Punctuation, '('),
        Token(T.Name, 'id'),
        Token(T.Operator, '='),
        Token(T.Number, '0'),
        Token(T.Punctuation, ')'),
        Token(T.Punctuation, ')'),
        Token(T.Punctuation, ';'),
    ]

    expected_tokens = TokenList([
        Token(T.Keyword, 'CREATE'),
        Token(T.Keyword, 'TABLE'),
        Token(T.Name, 'table_name'),
        Parenthesis([
            Token(T.Punctuation, '('),
            Token(T.Name, 'id'),
            Token(T.Keyword, 'SERIAL'),
            Token(T.Keyword, 'CHECK'),
            Parenthesis([
                Token(T.Punctuation, '('),
                Token(T.Name, 'id'),
                Token(T.Operator, '='),
                Token(T.Number, '0'),
                Token(T.Punctuation, ')'),
            ]),
            Token(T.Punctuation, ')'),
        ]),
        Token(T.Punctuation, ';'),
    ])

    grouped_tokens = group_parentheses(tokens)

    stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        expected_tokens._pprint_tree()
        a = sys.stdout.getvalue()
        sys.stdout = StringIO()
        grouped_tokens._pprint_tree()
        b = sys.stdout.getvalue()
    finally:
        sys.stdout = stdout

    assert_multi_line_equal(a, b)


def test_parse_statements():
    sql = '''
SET search_path = 'cover_art_archive';

CREATE TABLE table_name (
    id SERIAL, -- PK
    name VARCHAR
);

CREATE TYPE FLUENCY AS ENUM ('basic', 'intermediate', 'advanced', 'native');
    '''
    statements = sqlparse.parse(sql)
    for statement in statements:
        statement._pprint_tree()
        print()
    statements = parse_statements(statements)
    for statement in statements:
        print(repr(statement))


def test_set_statement():
    sql = "SET search_path = 'cover_art_archive';"
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, Set)
    assert_equal('search_path', statement.get_name())
    assert_equal('cover_art_archive', statement.get_value())


def test_set_statement_without_quotes():
    sql = "SET search_path = cover_art_archive;"
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, Set)
    assert_equal('search_path', statement.get_name())
    assert_equal('cover_art_archive', statement.get_value())


def test_set_statement_with_to():
    sql = "SET search_path TO 'cover_art_archive';"
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, Set)
    assert_equal('search_path', statement.get_name())
    assert_equal('cover_art_archive', statement.get_value())


def test_create_type_statement():
    sql = "CREATE TYPE FLUENCY AS ENUM ('basic', 'intermediate');"
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, CreateType)
    assert_equal('FLUENCY', statement.get_name())
    assert_equal(['basic', 'intermediate'], statement.get_enum_labels())


def test_create_table_statement():
    sql = '''
CREATE TABLE table_name (
    id SERIAL, -- PK
    name VARCHAR(100) NOT NULL,
    created TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL
);
    '''
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, CreateTable)
    assert_equal('table_name', statement.get_name())

    columns = list(statement.get_columns())
    assert_equal(3, len(columns))

    column = columns[0]
    assert_equal('id', column.get_name())
    assert_equal('SERIAL', column.get_type())
    assert_equal(None, column.get_default_value())
    assert_equal(['-- PK'], column.get_comments())
    assert_equal(False, column.is_not_null())
    assert_equal(None, column.get_check_constraint())

    column = columns[1]
    assert_equal('name', column.get_name())
    assert_equal('VARCHAR(100)', column.get_type())
    assert_equal(None, column.get_default_value())
    assert_equal([], column.get_comments())
    assert_equal(True, column.is_not_null())
    assert_equal(None, column.get_check_constraint())

    column = columns[2]
    assert_equal('created', column.get_name())
    assert_equal('TIMESTAMP WITH TIME ZONE', column.get_type())
    assert_equal('now()', column.get_default_value())
    assert_equal([], column.get_comments())
    assert_equal(True, column.is_not_null())
    assert_equal(None, column.get_check_constraint())


def test_create_table_statement_check_constraint():
    sql = '''CREATE TABLE table_name (column INTEGER(2) NOT NULL DEFAULT 0 CHECK (edits_pending > 0)); '''
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, CreateTable)
    columns = list(statement.get_columns())
    assert_equal(1, len(columns))

    column = columns[0]
    check = column.get_check_constraint()
    assert_true(check)
    assert_equal(None, check.get_name())
    assert_equal('edits_pending>0', str(check.get_body()))


def test_create_table_statement_named_check_constraint():
    sql = '''CREATE TABLE table_name (column INTEGER(2) NOT NULL DEFAULT 0 CONSTRAINT check_column CHECK (edits_pending > 0)); '''
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, CreateTable)
    columns = list(statement.get_columns())
    assert_equal(1, len(columns))

    column = columns[0]
    check = column.get_check_constraint()
    assert_true(check)
    assert_equal('check_column', check.get_name())
    assert_equal('edits_pending>0', str(check.get_body()))


def test_create_index():
    sql = '''CREATE INDEX statistic_name ON statistic (name); '''
    statement = next(parse_statements(sqlparse.parse(sql)))

    assert_is_instance(statement, CreateIndex)
    assert_equal('statistic_name', statement.get_name())
    assert_equal('statistic', statement.get_table())
    assert_equal(['name'], statement.get_columns())
    assert_false(statement.is_unique())


def test_create_unique_index():
    sql = '''CREATE UNIQUE INDEX statistic_name_date_collected ON statistic (name, date_collected); '''
    statement = next(parse_statements(sqlparse.parse(sql)))

    statement._pprint_tree()

    assert_is_instance(statement, CreateIndex)
    assert_equal('statistic_name_date_collected', statement.get_name())
    assert_equal('statistic', statement.get_table())
    assert_equal(['name', 'date_collected'], statement.get_columns())
    assert_true(statement.is_unique())
