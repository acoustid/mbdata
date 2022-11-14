import pytest

from mbdata.tools.genmodels import (
    format_model_name,
    parse_sql,
    convert_expression_to_python,
)


@pytest.mark.parametrize(
    "table_name, model_name",
    [
        ('artist', 'Artist'),
        ('recording_isrc', 'RecordingISRC'),
        ('l_artist_artist', 'LinkArtistArtist'),
        ('iso_3166_1', 'ISO31661'),
    ]
)
def test_format_model_name(table_name, model_name):
    assert format_model_name(table_name) == model_name


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

    tables, types, indexes = parse_sql(sql)

    assert 1 == len(types)

    assert 'cover_art_archive' == types[0].schema
    assert 'COVER_ART_TYPE' == types[0].name
    assert ['front', 'back'] == types[0].labels

    assert 2 == len(tables)

    assert 'musicbrainz' == tables[0].schema
    assert 'release' == tables[0].name
    assert 2 == len(tables[0].columns)
    assert 'id' == tables[0].columns[0].name
    assert 'SERIAL' == tables[0].columns[0].type
    assert True is tables[0].columns[0].primary_key
    assert None is tables[0].columns[0].foreign_key
    assert 'name' == tables[0].columns[1].name
    assert 'VARCHAR' == tables[0].columns[1].type
    assert False is tables[0].columns[1].primary_key
    assert None is tables[0].columns[1].foreign_key

    assert 'cover_art_archive' == tables[1].schema
    assert 'cover_art' == tables[1].name
    assert 3 == len(tables[1].columns)
    assert 'id' == tables[1].columns[0].name
    assert 'SERIAL' == tables[1].columns[0].type
    assert True is tables[1].columns[0].primary_key
    assert None is tables[1].columns[0].foreign_key
    assert 'release' == tables[1].columns[1].name
    assert 'INTEGER' == tables[1].columns[1].type
    assert False is tables[1].columns[1].primary_key
    assert 'musicbrainz' == tables[1].columns[1].foreign_key.schema
    assert 'release' == tables[1].columns[1].foreign_key.table
    assert 'id' == tables[1].columns[1].foreign_key.column
    assert 'type' == tables[1].columns[2].name
    assert 'COVER_ART_TYPE' == tables[1].columns[2].type
    assert False is tables[1].columns[2].primary_key
    assert None is tables[1].columns[2].foreign_key


def test_expression_to_python_binary_op_compare():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id >= 0));'''
    tables, types, indexes = parse_sql(sql)

    assert 1 == len(tables)
    assert 1 == len(tables[0].columns)
    check = tables[0].columns[0].check_constraint

    assert "sql.literal_column('id') >= sql.text('0')" == convert_expression_to_python(check.text)


def test_expression_to_python_is_null():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id IS NULL));'''
    tables, types, indexes = parse_sql(sql)

    assert 1 == len(tables)
    assert 1 == len(tables[0].columns)
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    assert "sql.literal_column('id') == None" == convert_expression_to_python(check.text)


def test_expression_to_python_is_not_null():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id IS NOT NULL));'''
    tables, types, indexes = parse_sql(sql)

    assert 1 == len(tables)
    assert 1 == len(tables[0].columns)
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    assert "sql.literal_column('id') != None" == convert_expression_to_python(check.text)


def test_expression_to_python_nested_op():
    sql = '''CREATE TABLE table (id SERIAL CHECK (((a IS NOT NULL OR b IS NOT NULL) AND c = TRUE) OR ((a IS NULL AND a IS NULL))));'''
    tables, types, indexes = parse_sql(sql)

    assert 1 == len(tables)
    assert 1 == len(tables[0].columns)
    check = tables[0].columns[0].check_constraint

    expected = (
        "sql.or_((sql.and_((sql.or_(sql.literal_column('a') != None, sql.literal_column('b') != None)), "
        "sql.literal_column('c') == sql.true())), ((sql.and_(sql.literal_column('a') == None, sql.literal_column('a') == None))))"
    )
    assert expected == convert_expression_to_python(check.text)


def test_expression_to_python_special_name():
    sql = '''CREATE TABLE table (length INTEGER CHECK (length IS NULL OR length > 0));'''
    tables, types, indexes = parse_sql(sql)

    assert 1 == len(tables)
    assert 1 == len(tables[0].columns)
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    expected = "sql.or_(sql.text('length') == None, sql.text('length') > sql.text('0'))"
    assert expected == convert_expression_to_python(check.text)


def test_expression_to_python_special_name_2():
    sql = '''CREATE TABLE table (date DATE NOT NULL CHECK (date >= '2000-01-01'));'''
    tables, types, indexes = parse_sql(sql)

    assert 1 == len(tables)
    assert 1 == len(tables[0].columns)
    check = tables[0].columns[0].check_constraint

    check.text._pprint_tree()
    expected = "sql.text('date') >= sql.text(\"'2000-01-01'\")"
    assert expected == convert_expression_to_python(check.text)


def test_expression_to_python_regex_op():
    sql = '''CREATE TABLE table (id SERIAL CHECK (id ~ E'^\\\\d{11}$'));'''
    tables, types, indexes = parse_sql(sql)

    assert 1 == len(tables)
    assert 1 == len(tables[0].columns)
    check = tables[0].columns[0].check_constraint

    expected = "regexp(sql.literal_column('id'), '^\\d{11}$')"
    assert expected == convert_expression_to_python(check.text)
