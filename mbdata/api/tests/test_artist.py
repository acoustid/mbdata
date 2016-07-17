# -*- coding: utf8 -*-

from nose.tools import *
from mbdata.api.tests import with_client, assert_json_response_equal


@with_client
def test_artist_get(client):
    rv = client.get('/v1/artist/get?id=95e9aba6-f85c-48a0-9ec9-395d4f0e3875&include=areas&include=ipi&include=isni&include=areas.part_of&include=areas.iso_3166&include=areas.type')

    expected = {
        u'response': {
            "artist": {
                "id": "95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                "name": u"Trentem\xf8ller", 
                "begin_date": {
                    "year": 1972, 
                    "day": 16, 
                    "month": 10
                }, 
                "area": {
                    "iso_3166_1": [
                        "DK"
                    ], 
                    "type": "Country", 
                    "name": "Denmark"
                }, 
                "gender": "Male", 
                "ipis": [
                    "00054968649", 
                    "00549686493"
                ], 
                "begin_area": {
                    "part_of": {
                        "part_of": {
                            "part_of": {
                                "iso_3166_1": [
                                    "DK"
                                ], 
                                "type": "Country", 
                                "name": "Denmark"
                            }, 
                            "iso_3166_2": [
                                "DK-85"
                            ], 
                            "type": "Subdivision", 
                            "name": "Region Zealand"
                        }, 
                        "type": "Municipality", 
                        "name": "Vordingborg Municipality"
                    }, 
                    "type": "City", 
                    "name": "Vordingborg"
                }, 
                "isnis": [
                    "0000000117742762"
                ], 
                "sort_name": u"Trentem\xf8ller", 
                "type": "Person", 
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
    rv = client.get('/v1/artist/get?id=89ad4ac3-39f7-470e-963a-56509c546377&include=areas&include=ipi&include=isni&include=areas.part_of')

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


@with_client
def test_artist_list_releases(client):
    rv = client.get('/v1/artist/list_releases?id=95e9aba6-f85c-48a0-9ec9-395d4f0e3875&include=mediums')

    expected = {
        u"response": {
            u"status": {
                u"message": u"success",
                u"code": 0,
                u"version": u"1.0"
            },
            u"releases": [
                {
                    u"status": u"Promotion",
                    u"name": u"Trentem\xf8ller: The P\xf8lar Mix",
                    u"language": u"English",
                    u"script": u"Latin",
                    u"mediums": [
                        {
                            u"position": 1,
                            u"track_count": 12,
                            u"format": u"CD"
                        },
                        {
                            u"position": 2,
                            u"track_count": 13,
                            u"format": u"CD"
                        }
                    ],
                    u"id": u"89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149"
                }
            ]
        }
    }

    assert_json_response_equal(rv, expected)


@with_client
def test_artist_list_release_groups(client):
    rv = client.get('/v1/artist/list_release_groups?id=95e9aba6-f85c-48a0-9ec9-395d4f0e3875')

    expected = {
        u"response": {
            u"status": {
                u"message": u"success",
                u"code": 0,
                u"version": u"1.0"
            },
            u"release_groups": [
                {
                    u"secondary_types": [u"Compilation"],
                    u"type": u"Album",
                    u"id": u"baca4e84-aa67-3ef9-adbe-0dfebe7b6a82",
                    u"name": u"Trentem\xf8ller: The P\xf8lar Mix"
                }
            ]
        }
    }

    assert_json_response_equal(rv, expected)

