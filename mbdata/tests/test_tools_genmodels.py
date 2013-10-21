from nose.tools import *
from mbdata.tools.genmodels import (
    format_model_name,
)


def check_format_model_name(table_name, model_name):
    assert_equals(format_model_name(table_name), model_name)


def test_format_model_name():
    names = [
        ('artist', 'Artist'),
        ('recording_isrc', 'RecordingISRC'),
        ('l_artist_artist', 'LinkArtistArtist'),
        ('iso_3166_1', 'ISO31661'),
    ]
    for table_name, model_name in names:
        yield check_format_model_name, table_name, model_name

