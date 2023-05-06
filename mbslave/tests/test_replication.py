from __future__ import print_function
import sys
import os
from six import StringIO
from mbslave.replication import (
    Config,
    remap_schema,
    join_paths,
    split_paths,
)


def test_remap_schema():
    config = Config(os.devnull)
    config.schemas.mapping['musicbrainz'] = 'mb'
    lines = ['CREATE SCHEMA musicbrainz;\n']
    expected_lines = ['CREATE SCHEMA mb;\n']
    actual_lines = list(remap_schema(config, lines))
    assert expected_lines == actual_lines


def test_join_and_split_paths():
    paths = ['a b', 'c']
    assert paths == split_paths(join_paths(paths))
