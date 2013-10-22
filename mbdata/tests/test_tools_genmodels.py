import sys
from nose.tools import *
from StringIO import StringIO
import sqlparse
from sqlparse import tokens as T
from sqlparse.sql import Token, TokenList, Parenthesis, Identifier
from mbdata.tools.genmodels import (
    format_model_name,
    parse_create_tables_sql,
    convert_expression_to_python,
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


def test_parse_create_tables_sql():
    sql = '''
CREATE TABLE release (
    id SERIAL, -- PK
    name VARCHAR NOT NULL
);

SET search_path = 'cover_art_archive';

CREATE TYPE COVER_ART_TYPE AS ENUM ('front', 'back');

CREATE TABLE cover_art (
    id SERIAL, -- PK
    release INTEGER NOT NULL, -- references musicbrainz.release.id
    type COVER_ART_TYPE
);
    '''

    types, tables = parse_create_tables_sql(sql)

    assert_equals(1, len(types))

    assert_equals('cover_art_archive', types[0].schema)
    assert_equals('COVER_ART_TYPE', types[0].name)
    assert_equals(['front', 'back'], types[0].labels)

    assert_equals(2, len(tables))

    assert_equals('musicbrainz', tables[0].schema)
    assert_equals('release', tables[0].name)
    assert_equals(2, len(tables[0].columns))
    assert_equals('id', tables[0].columns[0].name)
    assert_equals('SERIAL', tables[0].columns[0].type)
    assert_equals(True, tables[0].columns[0].primary_key)
    assert_equals(None, tables[0].columns[0].foreign_key)
    assert_equals('name', tables[0].columns[1].name)
    assert_equals('VARCHAR', tables[0].columns[1].type)
    assert_equals(False, tables[0].columns[1].primary_key)
    assert_equals(None, tables[0].columns[1].foreign_key)

    assert_equals('cover_art_archive', tables[1].schema)
    assert_equals('cover_art', tables[1].name)
    assert_equals(3, len(tables[1].columns))
    assert_equals('id', tables[1].columns[0].name)
    assert_equals('SERIAL', tables[1].columns[0].type)
    assert_equals(True, tables[1].columns[0].primary_key)
    assert_equals(None, tables[1].columns[0].foreign_key)
    assert_equals('release', tables[1].columns[1].name)
    assert_equals('INTEGER', tables[1].columns[1].type)
    assert_equals(False, tables[1].columns[1].primary_key)
    assert_equals('musicbrainz', tables[1].columns[1].foreign_key.schema)
    assert_equals('release', tables[1].columns[1].foreign_key.table)
    assert_equals('id', tables[1].columns[1].foreign_key.column)
    assert_equals('type', tables[1].columns[2].name)
    assert_equals('COVER_ART_TYPE', tables[1].columns[2].type)
    assert_equals(False, tables[1].columns[2].primary_key)
    assert_equals(None, tables[1].columns[2].foreign_key)


def test_expression_to_python_binary_op_compare():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id >= 0));'''
    types, tables = parse_create_tables_sql(sql)

    assert_equal(1, len(tables))
    assert_equal(1, len(tables[0].columns))
    check = tables[0].columns[0].check_constraint

    assert_equal("sql.literal_column('id') >= sql.text('0')", convert_expression_to_python(check.text))


def test_expression_to_python_is_null():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id IS NULL));'''
    types, tables = parse_create_tables_sql(sql)

    assert_equal(1, len(tables))
    assert_equal(1, len(tables[0].columns))
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    assert_equal("sql.literal_column('id') == None", convert_expression_to_python(check.text))


def test_expression_to_python_is_not_null():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id IS NOT NULL));'''
    types, tables = parse_create_tables_sql(sql)

    assert_equal(1, len(tables))
    assert_equal(1, len(tables[0].columns))
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    assert_equal("sql.literal_column('id') != None", convert_expression_to_python(check.text))


def test_expression_to_python_nested_op():
    sql = '''CREATE TABLE table (id SERIAL CHECK (((a IS NOT NULL OR b IS NOT NULL) AND c = TRUE) OR ((a IS NULL AND a IS NULL))));'''
    types, tables = parse_create_tables_sql(sql)

    assert_equal(1, len(tables))
    assert_equal(1, len(tables[0].columns))
    check = tables[0].columns[0].check_constraint

    expected = "sql.or_((sql.and_((sql.or_(sql.literal_column('a') != None, sql.literal_column('b') != None)), sql.literal_column('c') == sql.true())), ((sql.and_(sql.literal_column('a') == None, sql.literal_column('a') == None))))"
    assert_equal(expected, convert_expression_to_python(check.text))


def test_expression_to_python_special_name():
    sql = '''CREATE TABLE table (length INTEGER CHECK (length IS NULL OR length > 0));'''
    types, tables = parse_create_tables_sql(sql)

    assert_equal(1, len(tables))
    assert_equal(1, len(tables[0].columns))
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    expected = "sql.or_(sql.text('length') == None, sql.text('length') > sql.text('0'))"
    assert_equal(expected, convert_expression_to_python(check.text))


def test_expression_to_python_special_name_2():
    sql = '''CREATE TABLE table (date DATE NOT NULL CHECK (date >= '2000-01-01'));'''
    types, tables = parse_create_tables_sql(sql)

    assert_equal(1, len(tables))
    assert_equal(1, len(tables[0].columns))
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    expected = "sql.text('date') >= sql.text('2000-01-01')"
    assert_equal(expected, convert_expression_to_python(check.text))


def test_expression_to_python_regex_op():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id ~ E'^\\\\d{11}$'));'''
    types, tables = parse_create_tables_sql(sql)

    assert_equal(1, len(tables))
    assert_equal(1, len(tables[0].columns))
    check = tables[0].columns[0].check_constraint

    expected = "regexp(sql.literal_column('id'), '^\\d{11}$')"
    assert_equal(expected, convert_expression_to_python(check.text))

