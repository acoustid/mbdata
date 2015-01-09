# -*- coding: utf8 -*-

from nose.tools import *
from mbdata.api.tests import with_client, assert_json_response_equal


@with_client
def test_label_get(client):
    rv = client.get('/v1/label/get?id=ecc049d0-88a6-4806-a5b7-0f1367a7d6e1&include=area&include=ipi&include=isni')

    expected = {
        u"response": {
            u"status": {
                u"message": u"success",
                u"code": 0,
                u"version": u"1.0"
            },
            u"label": {
                u"begin_date": {
                    u"year": 1985,
                    u"month": 6
                },
                u"name": u"\u30b9\u30bf\u30b8\u30aa\u30b8\u30d6\u30ea",
                u"area": {
                    u"name": u"Japan"
                },
                u"ipis": [
                    u"00173517959",
                    u"00473554732"
                ],
                u"isnis": [
                    u"000000011781560X"
                ],
                u"type": u"Production",
                u"id": u"ecc049d0-88a6-4806-a5b7-0f1367a7d6e1"
            }
        }
    }

    assert_json_response_equal(rv, expected)

