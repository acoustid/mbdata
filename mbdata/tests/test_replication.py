from __future__ import print_function
import sys
import os
from nose.tools import assert_equal, assert_true, assert_false, assert_is_instance, assert_multi_line_equal
from six import StringIO
from mbdata.replication import (
    Config,
    remap_schema,
)


def test_remap_schema():
    config = Config(os.devnull)
    config.schemas.mapping['musicbrainz'] = 'mb'
    lines = ['CREATE SCHEMA musicbrainz;\n']
    expected_lines = ['CREATE SCHEMA mb;\n']
    actual_lines = list(remap_schema(config, lines))
    assert_equal(expected_lines, actual_lines)
