# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

import re
import itertools
from six import string_types
from mbdata.utils.models import ENTITY_TYPES
from typing import Set, Dict, Type


def _iter_includes(tokens):
    if isinstance(tokens, string_types):
        yield tokens
        return

    includes = ['']
    for token in tokens:
        if token == ',':
            for include in includes:
                yield include
            includes = ['']
        else:
            new_includes = []
            for prefix, suffix in itertools.product(includes, _iter_includes(token)):
                new_includes.append(prefix + suffix)
            includes = new_includes

    if includes != ['']:
        for include in includes:
            yield include


def expand_includes(input):
    tokens = re.split(r'([,()])', input)

    groups = [[]]
    for token in tokens:
        if token == '(':
            groups.append([])
        elif token == ')':
            group = groups.pop()
            groups[-1].append(group)
        elif token:
            groups[-1].append(token)
    grouped_tokens = groups.pop()

    return _iter_includes(grouped_tokens)


def expand_includes_multi(inputs):
    return itertools.chain.from_iterable(map(expand_includes, inputs))


class Includes(object):
    INCLUDES = set([])  # type: Set[str]
    SUB_INCLUDES = {}  # type: Dict[str, Type[Includes]]

    def __init__(self, includes=None, itself=True):
        self.includes = dict(includes or {})
        for name in self.SUB_INCLUDES:
            if name in self.includes and not isinstance(self.includes[name], Includes):
                self.includes[name] = self.SUB_INCLUDES[name]()
        self.itself = itself

    def check(self, name):
        try:
            return getattr(self, name)
        except AttributeError:
            return False

    def __bool__(self):
        return self.itself

    __nonzero__ = __bool__

    def __getattr__(self, name):
        if name not in self.INCLUDES and name not in self.SUB_INCLUDES:
            raise AttributeError(name)

        if name not in self.includes and name in self.SUB_INCLUDES:
            self.includes[name] = self.SUB_INCLUDES[name](itself=False)

        return self.includes.get(name, False)

    @classmethod
    def parse(cls, params, prefix=''):
        includes = {}
        sub_includes = {}

        for include in expand_includes_multi(params):
            if '.' in include:
                include, sub_include = include.split('.', 1)
            else:
                sub_include = None

            if include not in cls.INCLUDES and include not in cls.SUB_INCLUDES:
                raise ValueError('unknown include {0}{1}'.format(prefix, include))

            includes[include] = True

            if sub_include is not None:
                if include not in cls.SUB_INCLUDES:
                    raise ValueError("unknown include {0}{1}.{2}".format(prefix, include, sub_include))
                sub_includes.setdefault(include, []).append(sub_include)

        for include, sub_params in sub_includes.items():
            includes[include] = cls.SUB_INCLUDES[include].parse(sub_params, '{0}.'.format(include))

        return cls(includes)


class RelationshipsIncludes(Includes):
    INCLUDES = set(ENTITY_TYPES.keys())


class AreaIncludes(Includes):
    INCLUDES = set([
        'part_of',
        'iso_3166',
        'type',
    ])


class ArtistIncludes(Includes):
    INCLUDES = set([
        'ipi',
        'isni',
    ])

    SUB_INCLUDES = {
        'areas': AreaIncludes,
        'relationships': RelationshipsIncludes,
    }


class LabelIncludes(Includes):
    INCLUDES = set([
        'ipi',
        'isni',
    ])

    SUB_INCLUDES = {
        'area': AreaIncludes,
        'relationships': RelationshipsIncludes,
    }


class RecordingIncludes(Includes):
    INCLUDES = set([
        'artist',
        'artists',
        'isrc',
    ])

    SUB_INCLUDES = {
        'relationships': RelationshipsIncludes,
    }


class TrackIncludes(Includes):
    INCLUDES = set([
        'artist',
        'artists',
    ])

    SUB_INCLUDES = {
        'recording': RecordingIncludes,
    }


class MediumIncludes(Includes):
    INCLUDES = set([])  # type: Set[str]

    SUB_INCLUDES = {
        'tracks': TrackIncludes,
    }


class ReleaseGroupIncludes(Includes):
    INCLUDES = set([
        'artist',
        'artists',
    ])

    SUB_INCLUDES = {
        'relationships': RelationshipsIncludes,
    }


class ReleaseIncludes(Includes):
    INCLUDES = set([
        'artist',
        'artists',
    ])

    SUB_INCLUDES = {
        'mediums': MediumIncludes,
        'release_group': ReleaseGroupIncludes,
        'relationships': RelationshipsIncludes,
    }


class WorkIncludes(Includes):
    INCLUDES = set([
        'iswc',
    ])

    SUB_INCLUDES = {
        'relationships': RelationshipsIncludes,
    }


class PlaceIncludes(Includes):
    INCLUDES = set([])  # type: Set[str]

    SUB_INCLUDES = {
        'area': AreaIncludes,
        'relationships': RelationshipsIncludes,
    }


class URLIncludes(Includes):
    INCLUDES = set([])  # type: Set[str]

    SUB_INCLUDES = {
        'relationships': RelationshipsIncludes,
    }


# this can't be defined directly in the class because of circular dependency
RelationshipsIncludes.SUB_INCLUDES = {
    'artist': ArtistIncludes,
    'label': LabelIncludes,
    'place': PlaceIncludes,
    'recording': RecordingIncludes,
    'release': ReleaseIncludes,
    'release_group': ReleaseGroupIncludes,
    'url': URLIncludes,
    'work': WorkIncludes,
}

