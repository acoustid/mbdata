# -*- coding: utf8 -*-

from nose.tools import *
from mbdata.api.tests import with_client, assert_json_response_equal


@with_client
def test_place_get(client):
    rv = client.get('/v1/place/get?id=bd55aeb7-19d1-4607-a500-14b8479d3fed&include=area.part_of')

    expected = {
        u'response': {
            u'place': {
                u'id': u'bd55aeb7-19d1-4607-a500-14b8479d3fed',
                u'name': u'Abbey Road Studios',
                u'address': u"3 Abbey Road, St John's Wood, London",
                u'type': u'Studio',
                u'coordinates': {u'latitude': 51.53192, u'longitude': -0.17835},
                u"area": {
                    u"part_of": {
                        u"part_of": {
                            u"part_of": {
                                u"name": u"United Kingdom"
                            },
                            u"name": u"England"
                        },
                        u"name": u"London"
                    },
                    u"name": u"Westminster"
                },
                u'begin_date': {u'year': 1931},
            },
            u'status': {
                u'code': 0,
                u'message': u'success',
                u'version': u'1.0'
            }
        }
    }

    assert_json_response_equal(rv, expected)

