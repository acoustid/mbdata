import sys
from nose.tools import *
from StringIO import StringIO
import sqlparse
from sqlparse import tokens as T
from sqlparse.sql import Token, TokenList, Parenthesis, Identifier
from mbdata.tools.genmodels import (
    format_model_name,
    parse_create_tables_sql,
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

