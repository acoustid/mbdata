# -*- coding: utf8 -*-

from nose.tools import *
from mbdata.api.tests import with_client, assert_json_response_equal


@with_client
def test_place_get(client):
    rv = client.get('/v1/place/get?id=bd55aeb7-19d1-4607-a500-14b8479d3fed&include=area.part_of')

    expected = {
        u'response': {
            "place": {
                "begin_date": {
                    "year": 1931
                }, 
                "name": "Abbey Road Studios", 
                "area": {
                    "part_of": {
                        "part_of": {
                            "part_of": {
                                "part_of": {
                                    "name": "United Kingdom"
                                }, 
                                "name": "England"
                            }, 
                            "name": "London"
                        }, 
                        "name": "Westminster"
                    }, 
                    "name": "St John's Wood"
                }, 
                "coordinates": {
                    "latitude": 51.53192, 
                    "longitude": -0.17835
                }, 
                "address": "3 Abbey Road, St John's Wood, London", 
                "type": "Studio", 
                "id": "bd55aeb7-19d1-4607-a500-14b8479d3fed"
            },
            u'status': {
                u'code': 0,
                u'message': u'success',
                u'version': u'1.0'
            }
        }
    }

    assert_json_response_equal(rv, expected)

