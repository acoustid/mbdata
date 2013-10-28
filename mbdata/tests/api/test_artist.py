# -*- coding: utf8 -*-

from nose.tools import *
from mbdata.tests.api import with_client, assert_json_response_equal


@with_client
def test_artist_get(client):
    rv = client.get('/v1/artist/get?id=95e9aba6-f85c-48a0-9ec9-395d4f0e3875&include=areas&include=ipi&include=isni')

    expected = {
        u'response': {
            u'artist': {
                u'id': u'95e9aba6-f85c-48a0-9ec9-395d4f0e3875',
                u'name': u'Trentem\xf8ller',
                u'sort_name': u'Trentem\xf8ller',
                u'type': u'Person',
                u'gender': u'Male',
                u'area': u'Denmark',
                u'begin_area': u'Vordingborg Municipality',
                u'begin_date': {u'day': 16, u'month': 10, u'year': 1974},
                u"ipis": [
                    u"00054968649"
                ],
                u"isnis": [
                    u"0000000117742762"
                ],
            },
            u'status': {
                u'code': 0,
                u'message': u'success',
                u'version': u'1.0'
            }
        }
    }

    assert_json_response_equal(rv, expected)


@with_client
def test_artist_get_va(client):
    rv = client.get('/v1/artist/get?id=89ad4ac3-39f7-470e-963a-56509c546377&include=areas&include=ipi&include=isni')

    expected = {
        u'response': {
            u'artist': {
                u'id': u'89ad4ac3-39f7-470e-963a-56509c546377',
                u'name': u'Various Artists',
                u'sort_name': u'Various Artists',
                u"comment": u"add compilations to this artist",
                u'type': u'Other',
                u'ipis': [],
                u'isnis': [],
            },
            u'status': {
                u'code': 0,
                u'message': u'success',
                u'version': u'1.0'
            }
        }
    }

    assert_json_response_equal(rv, expected)

