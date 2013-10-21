import sys
from nose.tools import *
from StringIO import StringIO
import sqlparse
from sqlparse import tokens as T
from sqlparse.sql import Token, TokenList, Parenthesis, Identifier
from mbdata.tools.genmodels import (
    format_model_name,
    group_parentheses,
    parse_statements,
    Set,
    CreateTable,
    CreateType,
)


def check_format_model_name(table_name, model_name):
    assert_equals(format_model_name(table_name), model_name)


def test_format_model_name():
    names = [
        ('artist', 'Artist'),
        ('recording_isrc', 'RecordingISRC'),
        ('l_artist_artist', 'LinkArtistArtist'),
        ('iso_3166_1', 'ISO31661'),
    ]
    for table_name, model_name in names:
        yield check_format_model_name, table_name, model_name


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
        print
    statements = parse_statements(statements)
    for statement in statements:
        print repr(statement)


def test_set_statement():
    sql = "SET search_path = 'cover_art_archive';"
    statement = parse_statements(sqlparse.parse(sql)).next()

    assert_is_instance(statement, Set)
    assert_equals('search_path', statement.get_name())
    assert_equals('cover_art_archive', statement.get_value())


def test_set_statement_without_quotes():
    sql = "SET search_path = cover_art_archive;"
    statement = parse_statements(sqlparse.parse(sql)).next()

    statement._pprint_tree()
    assert_is_instance(statement, Set)
    assert_equals('search_path', statement.get_name())
    assert_equals('cover_art_archive', statement.get_value())


def test_set_statement_with_to():
    sql = "SET search_path TO 'cover_art_archive';"
    statement = parse_statements(sqlparse.parse(sql)).next()

    statement._pprint_tree()
    assert_is_instance(statement, Set)
    assert_equals('search_path', statement.get_name())
    assert_equals('cover_art_archive', statement.get_value())

