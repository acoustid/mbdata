import sys
from nose.tools import *
from StringIO import StringIO
from sqlparse import tokens as T
from sqlparse.sql import Token, TokenList
from mbdata.tools.genmodels import (
    format_model_name,
    group_parentheses,
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
        TokenList([
            Token(T.Punctuation, '('),
            Token(T.Name, 'id'),
            Token(T.Keyword, 'SERIAL'),
            Token(T.Keyword, 'CHECK'),
            TokenList([
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

