# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import argparse
import datetime
import re
import unicodedata
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import object_session
from sqlalchemy.orm.collections import InstrumentedList
from mbdata.models import (
    Area,
    Artist,
    Label,
    LinkAreaArea,
    Place,
    Recording,
    Release,
    ReleaseGroup,
    Work,
    URL,
)
from mbdata.utils.models import query_links
from typing import Dict, Set


RELEASE_GIDS = [
    '89b1b3ca-07cd-4f67-b9a7-3a3ba86d7149',
    '7643ee96-fe19-4b76-aa9a-e8af7d0e9d73',
]

PLACE_GIDS = [
    'bd55aeb7-19d1-4607-a500-14b8479d3fed',  # Abbey Road Studios
]

LABEL_GIDS = [
    'ecc049d0-88a6-4806-a5b7-0f1367a7d6e1',  # Studio Ghibli
]


counters = {}  # type: Dict[str, int]
in_progress = set()  # type: Set[str]
models = set()  # type: Set[str]


_unaccent_dict = {u'Æ': u'AE', u'æ': u'ae', u'Œ': u'OE', u'œ': u'oe', u'ß': 'ss'}
_re_latin_letter = re.compile(r"^(LATIN [A-Z]+ LETTER [A-Z]+) WITH")


def unaccent(string):
    result = []
    for char in string:
        if char in _unaccent_dict:
            char = _unaccent_dict[char]
        else:
            try:
                name = unicodedata.name(char)
                match = _re_latin_letter.search(name)
                if match:
                    char = unicodedata.lookup(match.group(1))
            except Exception:
                pass
        result.append(char)
    return "".join(result)


def name_to_variable(name):
    return re.sub('_+', '_', re.sub('[^0-9a-z]', '_', unaccent(name).lower())).strip('_')


def generate_name(obj):
    name = obj.__class__.__name__.lower()
    if hasattr(obj, 'name') and obj.name:
        suffix = name_to_variable(obj.name)
        if not suffix and hasattr(obj, 'sort_name') and obj.sort_name:
            suffix = name_to_variable(obj.sort_name)
        if suffix:
            name = '{0}_{1}'.format(name, suffix)
    elif name not in counters:
        counters[name] = 0

    if name in counters:
        counters[name] += 1
        name += '_{0}'.format(counters[name])
    else:
        counters[name] = 0

    return name


def dump_value(value):
    if isinstance(value, datetime.datetime):
        value = value.replace(tzinfo=None)
    return repr(value)


def find_name(output, names, obj):
    state = inspect(obj)
    mapper = state.mapper

    key = state.identity_key
    if key in in_progress:
        return None

    if key in names:
        return names[key]

    in_progress.add(key)
    models.add(obj.__class__.__name__)

    name = generate_name(obj)

    code = []
    code.append('{0} = {1}()'.format(name, obj.__class__.__name__))

    for attr in mapper.column_attrs:
        if sum([len(column.foreign_keys) for column in attr.columns]):
            continue
        value = getattr(obj, attr.key)
        if value is None:
            continue
        code.append('{0}.{1} = {2}'.format(name, attr.key, dump_value(value)))

    for attr in sorted(mapper.relationships, key=lambda attr: attr.key):
        value = getattr(obj, attr.key, None)
        if value is None:
            continue
        if isinstance(value, InstrumentedList):
            value_names = []
            for item in value:
                value_name = find_name(output, names, item)
                if value_name is not None:
                    value_names.append(value_name)
            if value_names:
                code.append('{0}.{1} = ['.format(name, attr.key))
                for value_name in value_names:
                    code.append('    {0},'.format(value_name))
                code.append(']')
        else:
            value_name = find_name(output, names, value)
            if value_name is not None:
                code.append('{0}.{1} = {2}'.format(name, attr.key, value_name))

    code.append('session.add({0})'.format(name))

    output.append('\n'.join(code))

    names[key] = name
    in_progress.remove(key)

    # special case -- dump parent relationships for areas
    if isinstance(obj, Area):
        session = object_session(obj)
        query = session.query(LinkAreaArea).\
            filter(LinkAreaArea.entity1_id == obj.id)
        for sub_obj in query:
            find_name(output, names, sub_obj)

    # special case -- dump artist/place/label/url relationships for "music" entities
    if isinstance(obj, (ReleaseGroup, Release, Recording, Work)):
        for target_model in (Artist, Place, Label, URL):
            for sub_obj in query_links(obj, target_model):
                find_name(output, names, sub_obj)

    # special case -- dump work relationships for recordings and works
    if isinstance(obj, (Recording, Work)):
        for sub_obj in query_links(obj, Work):
            find_name(output, names, sub_obj)

    return name


def dump_sample_data(session):
    output = []
    names = {}

    queries = [
        session.query(Release).filter(Release.gid.in_(RELEASE_GIDS)),
        session.query(Place).filter(Place.gid.in_(PLACE_GIDS)),
        session.query(Label).filter(Label.gid.in_(LABEL_GIDS)),
    ]
    for query in queries:
        for item in query:
            find_name(output, names, item)

    print('import datetime')
    models_to_import = list(sorted(models))
    while models_to_import:
        print('from mbdata.models import {0}'.format(', '.join(models_to_import[:5])))
        models_to_import = models_to_import[5:]
    print()
    print()

    print('def create_sample_data(session):')

    for line in '\n\n'.join(output).splitlines():
        if not line:
            print()
        else:
            print('    ' + line)

    print()
    print('    session.commit()')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='db_uri')
    args = parser.parse_args()

    engine = create_engine(args.db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    dump_sample_data(session)
