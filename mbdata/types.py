# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

import re
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import UserDefinedType
from sqlalchemy.sql.expression import ClauseElement, TextClause
try:
    from sqlalchemy.dialects.postgresql import UUID, SMALLINT, BIGINT, JSONB
except ImportError:
    from sqlalchemy.dialects.postgres import UUID, SMALLINT, BIGINT, JSONB


@compiles(UUID, 'sqlite')
def visit_uuid_sqlite(element, compiler, **kwargs):
    return 'CHAR(32)'


# XXX this should really serialize/deserialize to JSON
@compiles(JSONB, 'sqlite')
def visit_jsonb_sqlite(element, compiler, **kwargs):
    return 'TEXT'


class regexp(ClauseElement):
    def __init__(self, column, pattern):
        self.column = column
        self.pattern = TextClause(pattern)


@compiles(regexp)
def visit_regexp(element, compiler, **kwargs):
    return '{0} REGEXP {1}'.format(
        compiler.process(element.column),
        compiler.process(element.pattern))


@compiles(regexp, 'postgresql')
def visit_regexp_postgresql(element, compiler, **kwargs):
    return '{0} ~ {1}'.format(
        compiler.process(element.column),
        compiler.process(element.pattern))


class PartialDate(object):

    __slots__ = ('year', 'month', 'day')

    def __init__(self, year=None, month=None, day=None):
        self.year = year
        self.month = month
        self.day = day

    def __composite_values__(self):
        return self.year, self.month, self.day

    def __iter__(self):
        yield self.year
        yield self.month
        yield self.day

    def __repr__(self):
        return "{0.__class__.__name__}(year={0.year}, month={0.month}, day={0.day})".format(self)

    def __eq__(self, other):
        return isinstance(other, PartialDate) and \
            other.year == self.year and \
            other.month == self.month and \
            other.day == self.day

    def __ne__(self, other):
        return not self.__eq__(other)

    def __bool__(self):
        return bool(self.year or self.month or self.day)

    __nonzero__ = __bool__


class Point(UserDefinedType):

    # pylint: disable=W0223
    # pylint: disable=R0201

    def get_col_spec(self):
        return 'POINT'

    def bind_processor(self, dialect):
        def process(value):
            if value is None:
                return None
            return '({0},{1})'.format(value[0], value[1])
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None:
                return None
            match = re.match(r'\((-?[0-9.]+),(-?[0-9.]+)\)', value)
            return tuple([float(x) for x in match.groups()])
        return process


class Cube(UserDefinedType):

    # pylint: disable=W0223
    # pylint: disable=R0201

    def get_col_spec(self):
        return 'CUBE'

    def bind_processor(self, dialect):
        def process(value):
            if value is None:
                return None
            return value
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None:
                return None
            return value
        return process

