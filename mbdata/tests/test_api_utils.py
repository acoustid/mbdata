from nose.tools import *
from mbdata.api.utils import make_includes


def test_make_includes_valid():
    includes = make_includes('artist_credits')
    include = includes(['artist_credits'])
    assert_true(include.artist_credits)
    assert_false(include.isrcs)


def test_make_includes_invalid_code():
    includes = make_includes('foo')
    assert_raises(ValueError, includes, ['foo'])


def test_make_includes_invalid_params():
    includes = make_includes('foo')
    assert_raises(ValueError, includes, ['bar'])

