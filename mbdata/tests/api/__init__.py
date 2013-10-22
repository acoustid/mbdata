# -*- coding: utf8 -*-

import os
import tempfile
import logging
import json
import functools

os.environ['MBDATA_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')
from mbdata import patch_model_schemas, NO_SCHEMAS
from mbdata.api import app
from mbdata.models import Base
from mbdata.tests.api.sample_data import create_sample_data


use_file_db = True
#use_file_db = False

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

