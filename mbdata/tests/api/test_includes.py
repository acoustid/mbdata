from nose.tools import *
from mbdata.api.includes import ReleaseIncludes, MediumIncludes, TrackIncludes


def test_includes_getters_simple():
    include = ReleaseIncludes({'artist_credits': True})
    assert_raises(AttributeError, getattr, include, 'does_not_exist')
    assert_true(include.artist_credits)
    assert_false(include.mediums)


def test_includes_parse_dotted():
    include = ReleaseIncludes({'artist_credits': True, 'mediums': MediumIncludes({})})
    assert_raises(AttributeError, getattr, include, 'does_not_exist')
    assert_true(include.artist_credits)
    assert_true(include.mediums)
    assert_false(include.mediums.tracks)
    assert_false(include.mediums.tracks.artist_credits)


def test_includes_parse_dotted_deep():
    include = ReleaseIncludes({
        'artist_credits': True,
        'mediums': MediumIncludes({
            'tracks': TrackIncludes({
                'artist_credits': True,
            })
        })
    })
    assert_raises(AttributeError, getattr, include, 'does_not_exist')
    assert_true(include.artist_credits)
    assert_true(include.mediums)
    assert_true(include.mediums.tracks)
    assert_true(include.mediums.tracks.artist_credits)


def test_includes_parse_simple():
    include = ReleaseIncludes.parse(['artist_credits'])
    assert_true(include.artist_credits)


def test_includes_parse_simple_2():
    include = ReleaseIncludes.parse(['artist_credits', 'mediums'])
    assert_true(include.artist_credits)
    assert_true(include.mediums)
    assert_false(include.mediums.tracks)
    assert_false(include.mediums.tracks.artist_credits)


def test_includes_parse_dotted():
    include = ReleaseIncludes.parse(['artist_credits', 'mediums.tracks'])
    assert_true(include.artist_credits)
    assert_true(include.mediums)
    assert_true(include.mediums.tracks)
    assert_false(include.mediums.tracks.artist_credits)


def test_includes_parse_dotted_deep():
    include = ReleaseIncludes.parse(['artist_credits', 'mediums.tracks.artist_credits'])
    assert_true(include.artist_credits)
    assert_true(include.mediums)
    assert_true(include.mediums.tracks)
    assert_true(include.mediums.tracks.artist_credits)


def test_includes_parse_unknown_simple():
    assert_raises(ValueError, ReleaseIncludes.parse, ['does_not_exist'])


def test_includes_parse_unknown_dotted():
    assert_raises(ValueError, ReleaseIncludes.parse, ['artist_credits.does_not_exist'])
    assert_raises(ValueError, ReleaseIncludes.parse, ['mediums.does_not_exist'])

