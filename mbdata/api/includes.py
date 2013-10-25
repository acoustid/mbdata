# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.


class Includes(object):
    INCLUDES = set([])
    SUB_INCLUDES = {}

    def __init__(self, includes=None, itself=True):
        self.includes = dict(includes or {})
        for name in self.SUB_INCLUDES:
            if name not in self.includes:
                self.includes[name] = self.SUB_INCLUDES[name](itself=False)
            elif not isinstance(self.includes[name], Includes):
                self.includes[name] = self.SUB_INCLUDES[name]()
        self.itself = itself

    def __nonzero__(self):
        return self.itself

    def __getattr__(self, name):
        if name not in self.INCLUDES:
            raise AttributeError(name)

        return self.includes.get(name, False)

    @classmethod
    def parse(cls, params, prefix=''):
        print cls, "parse", params, prefix
        includes = {}
        sub_includes = {}

        for include in params:
            if '.' in include:
                include, sub_include = include.split('.', 1)
            else:
                sub_include = None

            if include not in cls.INCLUDES:
                raise ValueError('unknown include {0}{1}'.format(prefix, include))

            includes[include] = True

            if sub_include is not None:
                if include not in cls.SUB_INCLUDES:
                    raise ValueError("unknown include {0}{1}.{2}".format(prefix, include, sub_include))
                sub_includes.setdefault(include, []).append(sub_include)

        for include, sub_params in sub_includes.iteritems():
            includes[include] = cls.SUB_INCLUDES[include].parse(sub_params, '{0}.'.format(include))

        return cls(includes)


class ArtistIncludes(Includes):
    INCLUDES = set([
        'areas',
        'ipi',
        'isni',
    ])


class LabelIncludes(Includes):
    INCLUDES = set([
        'areas',
        'ipi',
        'isni',
    ])


class RecordingIncludes(Includes):
    INCLUDES = set([
        'artist',
        'artists',
        'isrc',
    ])


class TrackIncludes(Includes):
    INCLUDES = set([
        'artist',
        'artists',
        'recordings',
    ])

    SUB_INCLUDES = {
        'recordings': RecordingIncludes,
    }


class MediumIncludes(Includes):
    INCLUDES = set([
        'tracks',
    ])

    SUB_INCLUDES = {
        'tracks': TrackIncludes,
    }


class ReleaseGroupIncludes(Includes):
    INCLUDES = [
        'artist',
        'artists',
    ]


class ReleaseIncludes(Includes):
    INCLUDES = set([
        'artist',
        'artists',
        'mediums',
        'release_group',
    ])

    SUB_INCLUDES = {
        'mediums': MediumIncludes,
        'release_group': ReleaseGroupIncludes,
    }


class WorkIncludes(Includes):
    INCLUDES = [
        'iswc',
    ]

