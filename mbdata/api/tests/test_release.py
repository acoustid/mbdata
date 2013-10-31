# -*- coding: utf8 -*-

import copy
from nose.tools import *
from mbdata.api.tests import with_client, assert_json_response_equal


BASE_RESPONSE = {
    u'response': {
        u'release': {
            u'id': u'89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149',
            u'name': u'Trentem\xf8ller: The P\xf8lar Mix',
            u'status': u'Promotion',
            u'language': u'English',
            u'script': u'Latin',
        },
        u'status': {
            u'code': 0,
            u'message': u'success',
            u'version': u'1.0',
        }
    }
}


@with_client
def test_release_get_not_found(client):
    rv = client.get('/v1/release/get?id=331b6652-3faf-43e0-9ce2-0f2e76b941e8')
    assert_equal(rv.status_code, 404)


@with_client
def test_release_get(client):
    rv = client.get('/v1/release/get?id=89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149')

    expected = copy.deepcopy(BASE_RESPONSE)

    assert_json_response_equal(rv, expected)


@with_client
def test_release_get_artist(client):
    rv = client.get('/v1/release/get?id=89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149&include=artist')

    expected = copy.deepcopy(BASE_RESPONSE)
    expected[u'response'][u'release'][u'artist'] = u'Trentem\xf8ller'

    assert_json_response_equal(rv, expected)


@with_client
def test_release_get_artists(client):
    rv = client.get('/v1/release/get?id=89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149&include=artists')

    expected = copy.deepcopy(BASE_RESPONSE)
    expected[u'response'][u'release'][u'artists'] = [
        {
            u'id': u'95e9aba6-f85c-48a0-9ec9-395d4f0e3875',
            u'name': u'Trentem\xf8ller'
        }
    ]

    assert_json_response_equal(rv, expected)


@with_client
def test_release_get_tracks_with_artist_and_credits(client):
    rv = client.get('/v1/release/get?id=89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149&include=artist&include=artists')
    assert_equal(rv.status_code, 400)


@with_client
def test_release_get_mediums(client):
    rv = client.get('/v1/release/get?id=89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149&include=mediums')

    expected = copy.deepcopy(BASE_RESPONSE)
    expected[u'response'][u'release'][u'mediums'] = [
        {
            u'format': u'CD',
            u'position': 1,
            u'track_count': 12
        },
        {
            u'format': u'CD',
            u'position': 2,
            u'track_count': 13
        }
    ]

    assert_json_response_equal(rv, expected)


@with_client
def test_release_get_tracks_and_mediums(client):
    rv = client.get('/v1/release/get?id=89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149&include=mediums&include=mediums.tracks')

    expected = copy.deepcopy(BASE_RESPONSE)
    expected[u'response'][u'release'][u'mediums'] = [
        {
            u"format": u"CD",
            u"position": 1,
            u"tracks": [
                {
                    u"position": 1,
                    u"length": 176.333,
                    u"id": u"b88995a5-a161-3f0b-80c9-dc94917b363a",
                    u"name": u"Small Piano Piece"
                },
                {
                    u"position": 2,
                    u"length": 262.72,
                    u"id": u"6e336acb-deaf-3824-ba89-5b612e2a864c",
                    u"name": u"Fantomes"
                },
                {
                    u"position": 3,
                    u"length": 439.146,
                    u"id": u"46624227-728d-3e0f-9b49-8447e9f9bc96",
                    u"name": u"The Very Last Resort"
                },
                {
                    u"position": 4,
                    u"length": 230.0,
                    u"id": u"1c6b5b95-cc69-363b-9ddb-62acd8f5ba7e",
                    u"name": u"Miss You"
                },
                {
                    u"position": 5,
                    u"length": 207.346,
                    u"id": u"ff49a567-bde9-37da-b49b-9a37e59e475c",
                    u"name": u"De Carla a Pered"
                },
                {
                    u"position": 6,
                    u"length": 271.2,
                    u"id": u"de879ef5-c5c5-338a-a863-b3fd79a6b581",
                    u"name": u"Una"
                },
                {
                    u"position": 7,
                    u"length": 447.026,
                    u"id": u"8d32398e-757e-3d72-93c3-628671da9d38",
                    u"name": u"Snowflake"
                },
                {
                    u"position": 8,
                    u"length": 202.746,
                    u"id": u"bd12916b-0e92-3d06-8ac2-bea1a703e789",
                    u"name": u"Concentration (version 3)"
                },
                {
                    u"position": 9,
                    u"length": 302.813,
                    u"id": u"41256b61-9fa2-33e4-bc64-0dc266ede203",
                    u"name": u"Evil Dub"
                },
                {
                    u"position": 10,
                    u"length": 311.986,
                    u"id": u"ea027835-8081-36fc-a8d7-1f9fc9406f65",
                    u"name": u"Ghost Town"
                },
                {
                    u"position": 11,
                    u"length": 286.213,
                    u"id": u"3b1d1d75-20da-30c8-aec3-4907497a78fa",
                    u"name": u"Dubby Games"
                },
                {
                    u"position": 12,
                    u"length": 267.186,
                    u"id": u"fdf48b89-cd36-3256-8d87-489b48e04fdd",
                    u"name": u"Nightwalker"
                }
            ],
        },
        {
            u"format": u"CD",
            u"position": 2,
            u"tracks": [
                {
                    u"position": 1,
                    u"length": 408.48,
                    u"id": u"7a8a2335-e701-3fe1-ba15-d8d010b1b7b2",
                    u"name": u"Moan (feat. Ane Trolle)"
                },
                {
                    u"position": 2,
                    u"length": 288.96,
                    u"id": u"28a5b0cb-265e-3ad7-b300-4a39867640a4",
                    u"name": u"Break on Through (Dark Ride dub mix)"
                },
                {
                    u"position": 3,
                    u"length": 97.973,
                    u"id": u"0291a4dd-f5c0-3fce-aea0-516755e75a1f",
                    u"name": u"The Fallen (Justice remix)"
                },
                {
                    u"position": 4,
                    u"length": 149.506,
                    u"id": u"25a57cd3-77ce-39d6-952c-d3b91a5e59dc",
                    u"name": u"Nanny Nanny Boo Boo (Junior Senior remix)"
                },
                {
                    u"position": 5,
                    u"length": 153.226,
                    u"id": u"2fe80875-51a9-3a60-a253-0b99d3dc5edf",
                    u"name": u"Contort Yourself"
                },
                {
                    u"position": 6,
                    u"length": 149.373,
                    u"id": u"755abf8b-337f-3558-97e5-910ec05028c3",
                    u"name": u"Someone Like You"
                },
                {
                    u"position": 7,
                    u"length": 402.466,
                    u"id": u"081781bf-f10d-3406-ac7b-5df2aa03d0f1",
                    u"name": u"High on You"
                },
                {
                    u"position": 8,
                    u"length": 392.373,
                    u"id": u"9aa04088-f04b-3b98-8aa6-0d579de621fd",
                    u"name": u"Go! (Trentem\xf8ller remix)"
                },
                {
                    u"position": 9,
                    u"length": 14.986,
                    u"id": u"88d0b720-1aca-3513-8ab3-50d2a1293743",
                    u"name": u"Silent Shout (Trente short edit)"
                },
                {
                    u"position": 10,
                    u"length": 383.32,
                    u"id": u"8a14c288-f753-3c2b-9cb0-306b3eca70dc",
                    u"name": u"Feelin' Good (Trentem\xf8ller remix)"
                },
                {
                    u"position": 11,
                    u"length": 144.373,
                    u"id": u"e23716f6-6900-356a-bb73-b1b0e5e26b4d",
                    u"name": u"Beau Mot Plage (Freeform Five remix re-edit)"
                },
                {
                    u"position": 12,
                    u"length": 461.706,
                    u"id": u"258b1498-0b8d-30a5-a2fc-2ea92c4957b7",
                    u"name": u"Always Something Better (feat. Richard Davis)"
                },
                {
                    u"position": 13,
                    u"length": 356.16,
                    u"id": u"7d3c3101-db47-34dd-807f-a125afba6631",
                    u"name": u"We Share Our Mother's Health (Trentem\xf8ller remix)"
                }
            ],
        }
    ]

    assert_json_response_equal(rv, expected)


@with_client
def test_release_get_tracks_and_mediums_and_artists(client):
    rv = client.get('/v1/release/get?id=89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149&include=mediums&include=mediums.tracks&include=mediums.tracks.artists&include=artists')

    expected = copy.deepcopy(BASE_RESPONSE)
    expected[u'response'][u'release'][u'artists'] = [
        {
            u'id': u'95e9aba6-f85c-48a0-9ec9-395d4f0e3875',
            u'name': u'Trentem\xf8ller'
        }
    ]
    expected[u'response'][u'release'][u'mediums'] = [
        {
            u"format": u"CD",
            u"position": 1,
            u"tracks": [
                {
                    u"position": 1,
                    u"length": 176.333,
                    u"id": u"b88995a5-a161-3f0b-80c9-dc94917b363a",
                    u"name": u"Small Piano Piece",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                },
                {
                    u"position": 2,
                    u"length": 262.72,
                    u"id": u"6e336acb-deaf-3824-ba89-5b612e2a864c",
                    u"name": u"Fantomes",
                    u"artists": [
                        {
                            u"id": u"a50084a5-7009-47a1-81b7-1bb18d09bda4",
                            u"name": u"Khan"
                        }
                    ]
                },
                {
                    u"position": 3,
                    u"length": 439.146,
                    u"id": u"46624227-728d-3e0f-9b49-8447e9f9bc96",
                    u"name": u"The Very Last Resort",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                },
                {
                    u"position": 4,
                    u"length": 230.0,
                    u"id": u"1c6b5b95-cc69-363b-9ddb-62acd8f5ba7e",
                    u"name": u"Miss You",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                },
                {
                    u"position": 5,
                    u"length": 207.346,
                    u"id": u"ff49a567-bde9-37da-b49b-9a37e59e475c",
                    u"name": u"De Carla a Pered",
                    u"artists": [
                        {
                            u"id": u"95db1c7c-21b8-4956-82ad-20217cd5d395",
                            u"name": u"Lhasa"
                        }
                    ]
                },
                {
                    u"position": 6,
                    u"length": 271.2,
                    u"id": u"de879ef5-c5c5-338a-a863-b3fd79a6b581",
                    u"name": u"Una",
                    u"artists": [
                        {
                            u"id": u"e8d1f02e-7e77-4415-85b6-dc17e08debbf",
                            u"name": u"Murcof"
                        }
                    ]
                },
                {
                    u"position": 7,
                    u"length": 447.026,
                    u"id": u"8d32398e-757e-3d72-93c3-628671da9d38",
                    u"name": u"Snowflake",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                },
                {
                    u"position": 8,
                    u"length": 202.746,
                    u"id": u"bd12916b-0e92-3d06-8ac2-bea1a703e789",
                    u"name": u"Concentration (version 3)",
                    u"artists": [
                        {
                            u"id": u"41ee41ff-cec6-46a6-8e67-5991a8ebc2ed",
                            u"name": u"The Crystalites"
                        }
                    ]
                },
                {
                    u"position": 9,
                    u"length": 302.813,
                    u"id": u"41256b61-9fa2-33e4-bc64-0dc266ede203",
                    u"name": u"Evil Dub",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                },
                {
                    u"position": 10,
                    u"length": 311.986,
                    u"id": u"ea027835-8081-36fc-a8d7-1f9fc9406f65",
                    u"name": u"Ghost Town",
                    u"artists": [
                        {
                            u"id": u"07eb40a2-2914-439c-a01d-15a685b84ddf",
                            u"name": u"The Specials"
                        }
                    ]
                },
                {
                    u"position": 11,
                    u"length": 286.213,
                    u"id": u"3b1d1d75-20da-30c8-aec3-4907497a78fa",
                    u"name": u"Dubby Games",
                    u"artists": [
                        {
                            u"id": u"ac6eaeb6-a855-41a1-a461-f23dd292513c",
                            u"name": u"Businessman"
                        }
                    ]
                },
                {
                    u"position": 12,
                    u"length": 267.186,
                    u"id": u"fdf48b89-cd36-3256-8d87-489b48e04fdd",
                    u"name": u"Nightwalker",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                }
            ],
        },
        {
            u"format": u"CD",
            u"position": 2,
            u"tracks": [
                {
                    u"position": 1,
                    u"length": 408.48,
                    u"id": u"7a8a2335-e701-3fe1-ba15-d8d010b1b7b2",
                    u"name": u"Moan (feat. Ane Trolle)",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                },
                {
                    u"position": 2,
                    u"length": 288.96,
                    u"id": u"28a5b0cb-265e-3ad7-b300-4a39867640a4",
                    u"name": u"Break on Through (Dark Ride dub mix)",
                    u"artists": [
                        {
                            u"id": u"9efff43b-3b29-4082-824e-bc82f646f93d",
                            u"name": u"The Doors"
                        }
                    ]
                },
                {
                    u"position": 3,
                    u"length": 97.973,
                    u"id": u"0291a4dd-f5c0-3fce-aea0-516755e75a1f",
                    u"name": u"The Fallen (Justice remix)",
                    u"artists": [
                        {
                            u"id": u"aa7a2827-f74b-473c-bd79-03d065835cf7",
                            u"name": u"Franz Ferdinand"
                        }
                    ]
                },
                {
                    u"position": 4,
                    u"length": 149.506,
                    u"id": u"25a57cd3-77ce-39d6-952c-d3b91a5e59dc",
                    u"name": u"Nanny Nanny Boo Boo (Junior Senior remix)",
                    u"artists": [
                        {
                            u"id": u"2d67239c-aa40-4ad5-a807-9052b66857a6",
                            u"name": u"Le Tigre"
                        }
                    ]
                },
                {
                    u"position": 5,
                    u"length": 153.226,
                    u"id": u"2fe80875-51a9-3a60-a253-0b99d3dc5edf",
                    u"name": u"Contort Yourself",
                    u"artists": [
                        {
                            u"id": u"4e303fcf-0f7e-42f4-b84e-454a7922e725",
                            u"name": u"James White and The Blacks"
                        }
                    ]
                },
                {
                    u"position": 6,
                    u"length": 149.373,
                    u"id": u"755abf8b-337f-3558-97e5-910ec05028c3",
                    u"name": u"Someone Like You",
                    u"artists": [
                        {
                            u"id": u"f07c698b-f559-4dd0-a65b-b7fddd30355b",
                            u"name": u"Revl9n"
                        }
                    ]
                },
                {
                    u"position": 7,
                    u"length": 402.466,
                    u"id": u"081781bf-f10d-3406-ac7b-5df2aa03d0f1",
                    u"name": u"High on You",
                    u"artists": [
                        {
                            u"id": u"25fdd039-edad-466e-b150-d7405c4da995",
                            u"name": u"Thomas Schumacher"
                        }
                    ]
                },
                {
                    u"position": 8,
                    u"length": 392.373,
                    u"id": u"9aa04088-f04b-3b98-8aa6-0d579de621fd",
                    u"name": u"Go! (Trentem\xf8ller remix)",
                    u"artists": [
                        {
                            u"id": u"8970d868-0723-483b-a75b-51088913d3d4",
                            u"name": u"Moby"
                        }
                    ]
                },
                {
                    u"position": 9,
                    u"length": 14.986,
                    u"id": u"88d0b720-1aca-3513-8ab3-50d2a1293743",
                    u"name": u"Silent Shout (Trente short edit)",
                    u"artists": [
                        {
                            u"id": u"bf710b71-48e5-4e15-9bd6-96debb2e4e98",
                            u"name": u"The Knife"
                        }
                    ]
                },
                {
                    u"position": 10,
                    u"length": 383.32,
                    u"id": u"8a14c288-f753-3c2b-9cb0-306b3eca70dc",
                    u"name": u"Feelin' Good (Trentem\xf8ller remix)",
                    u"artists": [
                        {
                            u"id": u"e1c79c85-44ed-4483-8ec6-28cfe6440345",
                            u"name": u"Jokke Ils\xf8e"
                        }
                    ]
                },
                {
                    u"position": 11,
                    u"length": 144.373,
                    u"id": u"e23716f6-6900-356a-bb73-b1b0e5e26b4d",
                    u"name": u"Beau Mot Plage (Freeform Five remix re-edit)",
                    u"artists": [
                        {
                            u"id": u"4c99c0b4-5d46-44d2-8c49-ba47a522b016",
                            u"name": u"Isol\xe9e"
                        }
                    ]
                },
                {
                    u"position": 12,
                    u"length": 461.706,
                    u"id": u"258b1498-0b8d-30a5-a2fc-2ea92c4957b7",
                    u"name": u"Always Something Better (feat. Richard Davis)",
                    u"artists": [
                        {
                            u"id": u"95e9aba6-f85c-48a0-9ec9-395d4f0e3875",
                            u"name": u"Trentem\xf8ller"
                        }
                    ]
                },
                {
                    u"position": 13,
                    u"length": 356.16,
                    u"id": u"7d3c3101-db47-34dd-807f-a125afba6631",
                    u"name": u"We Share Our Mother's Health (Trentem\xf8ller remix)",
                    u"artists": [
                        {
                            u"id": u"bf710b71-48e5-4e15-9bd6-96debb2e4e98",
                            u"name": u"The Knife"
                        }
                    ]
                }
            ],
        }

    ]

    assert_json_response_equal(rv, expected)

