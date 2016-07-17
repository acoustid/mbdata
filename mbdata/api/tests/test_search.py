# XXX should be in mbdata/tests/

from nose.tools import *
from mbdata.api.tests import with_database
from mbdata.models import Artist, Label
from mbdata.search import schema, iter_data_entity


def data_to_dict(results):
    results = list(results)
    assert_equal(len(results), 1)
    data = {}
    for name, value in sorted(results[0][1]):
        data.setdefault(name, []).append(value)
    return data


@with_database
def test_export_artist(db):
    results = iter_data_entity(db, schema['artist'],
        Artist.gid == '95e9aba6-f85c-48a0-9ec9-395d4f0e3875')
    data = data_to_dict(results)
    assert_dict_equal(data, {
        'id': ['artist:108703'],
        'kind': ['artist'],
        'area': [u'Denmark'],
        'gender': [u'Male'],
        'ipi': [u'00054968649', u'00549686493'],
        'isni': [u'0000000117742762'],
        'mbid': [u'95e9aba6-f85c-48a0-9ec9-395d4f0e3875'],
        'name': [u'Trentem\xf8ller'],
        'sort_name': [u'Trentem\xf8ller'],
        'type': [u'Person'],
    })


@with_database
def test_export_label(db):
    results = iter_data_entity(db, schema['label'],
        Label.gid == 'ecc049d0-88a6-4806-a5b7-0f1367a7d6e1')
    data = data_to_dict(results)
    assert_dict_equal(data, {
        'id': ['label:83683'],
        'kind': ['label'],
        'area': [u'Japan'],
        'ipi': [u'00173517959', u'00473554732'],
        'isni': [u'000000011781560X'],
        'mbid': [u'ecc049d0-88a6-4806-a5b7-0f1367a7d6e1'],
        'name': [u'\u30b9\u30bf\u30b8\u30aa\u30b8\u30d6\u30ea'],
        'type': [u'Production'],
    })

