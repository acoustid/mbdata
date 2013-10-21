# -*- coding: utf8 -*-

import os
import tempfile
import logging
import json
import functools

os.environ['MBDATA_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')
from mbdata import patch_model_schemas, NO_SCHEMAS
from mbdata.api import app
from mbdata.models import Base, Artist, ArtistType, Gender


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
    insert_sample_data(session)
    session.close()


def teardown_package():
    if use_file_db:
        os.close(db_fd)
        os.unlink(db_name)


def insert_sample_data(session):
    group = ArtistType()
    group.name = 'Group'
    session.add(group)

    person = ArtistType()
    person.name = 'Person'
    session.add(person)

    male = Gender()
    male.name = 'Male'
    session.add(male)

    female = Gender()
    female.name = 'Female'
    session.add(female)

    artist = Artist()
    artist.gid = 'ce89261a-79cf-409e-a167-b4515b5eb5bb'
    artist.name = 'The Chemical Brothers'
    artist.sort_name = 'Chemical Brothers, The'
    artist.type = group
    session.add(artist)

    artist = Artist()
    artist.gid = '6655955b-1c1e-4bcb-84e4-81bcd9efab30'
    artist.name = u'Ólafur Arnalds'
    artist.sort_name = u'Arnalds, Ólafur'
    artist.type = person
    artist.gender = male
    session.add(artist)

    session.commit()


def with_client(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with app.app.test_client() as client:
            return func(client, *args, **kwargs)
    return wrapper

