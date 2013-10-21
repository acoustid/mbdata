# -*- coding: utf8 -*-

import json
from nose.tools import *
from mbdata.tests.api import with_client


@with_client
def test_artist_details_group(client):
    rv = client.get('/1.0/artist/details?id=ce89261a-79cf-409e-a167-b4515b5eb5bb')

    expected = {
        u'response': {
            u'artist': {
                u'id': u'ce89261a-79cf-409e-a167-b4515b5eb5bb',
                u'name': u'The Chemical Brothers',
                u'sort_name': u'Chemical Brothers, The',
                u'type': u'Group',
            },
            u'status': {
                u'code': 0,
                u'message': u'success',
                u'version': u'1.0'
            }
        }
    }

    assert_equal(200, rv.status_code)
    assert_dict_equal(expected, json.loads(rv.data))


@with_client
def test_artist_details_person(client):
    rv = client.get('/1.0/artist/details?id=6655955b-1c1e-4bcb-84e4-81bcd9efab30')

    expected = {
        u'response': {
            u'artist': {
                u'id': u'6655955b-1c1e-4bcb-84e4-81bcd9efab30',
                u'name': u'Ólafur Arnalds',
                u'sort_name': u'Arnalds, Ólafur',
                u'type': u'Person',
                u'gender': u'Male',
            },
            u'status': {
                u'code': 0,
                u'message': u'success',
                u'version': u'1.0'
            }
        }
    }

    assert_equal(200, rv.status_code)
    assert_dict_equal(expected, json.loads(rv.data))

