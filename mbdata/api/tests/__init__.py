# -*- coding: utf8 -*-

from __future__ import print_function
import os
import tempfile
import logging
import json
import functools
import pprint
import difflib
from unittest import TestCase
from unittest.util import safe_repr
from nose.tools import *
from flask import g

os.environ['MBDATA_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')
from mbdata.api import app
from mbdata.models import Base
from mbdata.utils import patch_model_schemas, NO_SCHEMAS
from mbdata.sample_data import create_sample_data


use_file_db = False

db_fd = db_name = None


def setup_package():
    global db_fd, db_name

    app.app.config['TESTING'] = True

    if use_file_db:
        db_fd, db_name = tempfile.mkstemp()
        app.app.config['DATABASE_URI'] = 'sqlite:///{0}'.format(db_name)
    else:
        app.app.config['DATABASE_URI'] = 'sqlite:///:memory:'

    app.setup_db()

    patch_model_schemas(NO_SCHEMAS)
    Base.metadata.create_all(app.engine)

    session = app.Session()
    create_sample_data(session)
    session.close()

    if os.environ.get('MBDATA_DATABASE_ECHO'):
        app.app.config['DATABASE_ECHO'] = True
        app.setup_db()


def teardown_package():
    if use_file_db:
        os.close(db_fd)
        os.unlink(db_name)


def with_client(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with app.app.test_client() as client:
            return func(client, *args, **kwargs)
    return wrapper


def with_database(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with app.app.test_request_context('/'):
            app.app.preprocess_request()
            return func(g.db, *args, **kwargs)
    return wrapper


class DummyTestCase(TestCase):

    def nop(self):
        pass


t = DummyTestCase('nop')


def assert_dict_equal(d1, d2):
    assert_is_instance(d1, dict, 'First argument is not a dictionary')
    assert_is_instance(d2, dict, 'Second argument is not a dictionary')

    if d1 != d2:
        standard_msg = '%s != %s' % (safe_repr(d1, True), safe_repr(d2, True))
        standard_msg += '\n'
        standard_msg += '\n'.join(difflib.unified_diff(
            json.dumps(d2, indent=4, ensure_ascii=False, sort_keys=True).splitlines(),
            json.dumps(d1, indent=4, ensure_ascii=False, sort_keys=True).splitlines(),
            '(expected)', '(actual)', lineterm=''
        ))
        t.fail(standard_msg)


def assert_json_response_equal(rv, expected):
    assert_equal(rv.status_code, 200, 'expected 200, got {0} with data {1!r}'.format(rv.status_code, rv.data))
    assert_equal(rv.content_type, 'application/json; charset=UTF-8')
    actual = json.loads(rv.data.decode('utf8'))
    try:
        assert_dict_equal(actual, expected)
    except AssertionError:
        print('Complete response:')
        print(json.dumps(actual, indent=4, ensure_ascii=False))
        raise

