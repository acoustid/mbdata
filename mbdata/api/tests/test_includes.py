from nose.tools import *
from mbdata.api.includes import ReleaseIncludes, MediumIncludes, TrackIncludes, expand_includes


def check_expand_includes(input, output):
    assert_equal(list(expand_includes(input)), output)


def test_expand_includes():
    test_cases = [
        ('artists', [
            'artists',
        ]),
        ('artists,mediums.tracks', [
            'artists',
            'mediums.tracks',
        ]),
        ('artists,mediums.tracks.(artists,recording)', [
            'artists',
            'mediums.tracks.artists',
            'mediums.tracks.recording',
        ]),
    ]
    for input, output in test_cases:
        yield check_expand_includes, input, output


def test_includes_getters_simple():
    include = ReleaseIncludes({'artists': True})
    assert_raises(AttributeError, getattr, include, 'does_not_exist')
    assert_true(include.artists)
    assert_false(include.mediums)


def test_includes_parse_dotted():
    include = ReleaseIncludes({'artists': True, 'mediums': MediumIncludes({})})
    assert_raises(AttributeError, getattr, include, 'does_not_exist')
    assert_true(include.artists)
    assert_true(include.mediums)
    assert_false(include.mediums.tracks)
    assert_false(include.mediums.tracks.artists)


def test_includes_parse_dotted_deep():
    include = ReleaseIncludes({
        'artists': True,
        'mediums': MediumIncludes({
            'tracks': TrackIncludes({
                'artists': True,
            })
        })
    })
    assert_raises(AttributeError, getattr, include, 'does_not_exist')
    assert_true(include.artists)
    assert_true(include.mediums)
    assert_true(include.mediums.tracks)
    assert_true(include.mediums.tracks.artists)


def test_includes_parse_simple():
    include = ReleaseIncludes.parse(['artists'])
    assert_true(include.artists)


def test_includes_parse_simple_2():
    include = ReleaseIncludes.parse(['artists', 'mediums'])
    assert_true(include.artists)
    assert_true(include.mediums)
    assert_false(include.mediums.tracks)
    assert_false(include.mediums.tracks.artists)


def test_includes_parse_dotted2():
    include = ReleaseIncludes.parse(['artists', 'mediums.tracks'])
    assert_true(include.artists)
    assert_true(include.mediums)
    assert_true(include.mediums.tracks)
    assert_false(include.mediums.tracks.artists)


def test_includes_parse_dotted2_deep():
    include = ReleaseIncludes.parse(['artists', 'mediums.tracks.artists'])
    assert_true(include.artists)
    assert_true(include.mediums)
    assert_true(include.mediums.tracks)
    assert_true(include.mediums.tracks.artists)


def test_includes_parse_dotted_deep_params():
    include = ReleaseIncludes.parse(['artists', 'mediums.tracks.(artists,recording.relationships.(artist,work))'])
    assert_true(include.artists)
    assert_true(include.mediums)
    assert_true(include.mediums.tracks)
    assert_true(include.mediums.tracks.artists)
    assert_true(include.mediums.tracks.recording)
    assert_true(include.mediums.tracks.recording.relationships)
    assert_true(include.mediums.tracks.recording.relationships.artist)
    assert_true(include.mediums.tracks.recording.relationships.work)


def test_includes_parse_unknown_simple():
    assert_raises(ValueError, ReleaseIncludes.parse, ['does_not_exist'])


def test_includes_parse_unknown_dotted():
    assert_raises(ValueError, ReleaseIncludes.parse, ['artists.does_not_exist'])
    assert_raises(ValueError, ReleaseIncludes.parse, ['mediums.does_not_exist'])

