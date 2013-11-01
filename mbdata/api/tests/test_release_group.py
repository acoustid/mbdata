# -*- coding: utf8 -*-

from nose.tools import *
from mbdata.api.tests import with_client, assert_json_response_equal


@with_client
def test_release_group_get(client):
    rv = client.get('/v1/release_group/get?id=baca4e84-aa67-3ef9-adbe-0dfebe7b6a82')

    expected = {
        u"response": {
            u"status": {
                u"message": u"success",
                u"code": 0,
                u"version": u"1.0"
            },
            u"release_group": {
                u"id": u"baca4e84-aa67-3ef9-adbe-0dfebe7b6a82",
                u"name": u"Trentem\xf8ller: The P\xf8lar Mix",
                u"type": u"Album",
                u"secondary_types": [u"Compilation"]
            }
        }
    }

    assert_json_response_equal(rv, expected)


@with_client
def test_release_group_list_releases(client):
    rv = client.get('/v1/release_group/list_releases?id=baca4e84-aa67-3ef9-adbe-0dfebe7b6a82&include=mediums')

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

