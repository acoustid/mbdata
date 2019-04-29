##########################
MusicBrainz Database Tools
##########################

****************************
MusicBrainz Database Replica
****************************

This repository now contains a collection of scripts for managing a
replica of the MusicBrainz database. These used to be called "mbslave",
but have been moved to this repository.

The main motivation for these scripts is to be able to customize
your database. If you don't need such custimizations, it might be
easier to use the replication tools provided by MusicBrainz itself.

Installation
============

 0. Make sure you have [Python 2](http://python.org/) and [psycopg2](http://initd.org/psycopg/) installed.
    On Debian and Ubuntu, that means installing these packages:

        sudo apt install python python-psycopg2

 1. Create `mbslave.conf` by copying and editing `mbslave.conf.default`.
    You will need to get the API token on the [MetaBrainz website](https://metabrainz.org/supporters/account-type).

 1. Setup the database. If you are starting completely from scratch,
    you can use the following commands to setup a clean database:

        sudo su - postgres
        createuser musicbrainz
        createdb -l C -E UTF-8 -T template0 -O musicbrainz musicbrainz
        createlang plpgsql musicbrainz
        psql musicbrainz -c 'CREATE EXTENSION cube;'
        psql musicbrainz -c 'CREATE EXTENSION earthdistance;'

 2. Prepare empty schemas for the MusicBrainz database and create the table structure:

        echo 'CREATE SCHEMA musicbrainz;' | ./mbslave-psql.py -S
        echo 'CREATE SCHEMA statistics;' | ./mbslave-psql.py -S
        echo 'CREATE SCHEMA cover_art_archive;' | ./mbslave-psql.py -S
        echo 'CREATE SCHEMA wikidocs;' | ./mbslave-psql.py -S
        echo 'CREATE SCHEMA documentation;' | ./mbslave-psql.py -S

        mbslave remap-schema <sql/CreateTables.sql | ./mbslave-psql.py
        mbslave remap-schema <sql/statistics/CreateTables.sql | ./mbslave-psql.py
        mbslave remap-schema <sql/caa/CreateTables.sql | ./mbslave-psql.py
        mbslave remap-schema <sql/wikidocs/CreateTables.sql | ./mbslave-psql.py
        mbslave remap-schema <sql/documentation/CreateTables.sql | ./mbslave-psql.py

 3. Download the MusicBrainz database dump files from
    http://ftp.musicbrainz.org/pub/musicbrainz/data/fullexport/

 4. Import the data dumps, for example:

        mbslave import mbdump.tar.bz2 mbdump-derived.tar.bz2

 5. Setup primary keys, indexes and views:

        ./mbslave-remap-schema.py <sql/CreatePrimaryKeys.sql | ./mbslave-psql.py
        ./mbslave-remap-schema.py <sql/statistics/CreatePrimaryKeys.sql | ./mbslave-psql.py
        ./mbslave-remap-schema.py <sql/caa/CreatePrimaryKeys.sql | ./mbslave-psql.py
        ./mbslave-remap-schema.py <sql/wikidocs/CreatePrimaryKeys.sql | ./mbslave-psql.py
        ./mbslave-remap-schema.py <sql/documentation/CreatePrimaryKeys.sql | ./mbslave-psql.py

        ./mbslave-remap-schema.py <sql/CreateIndexes.sql | grep -v musicbrainz_collate | ./mbslave-psql.py
        ./mbslave-remap-schema.py <sql/CreateSlaveIndexes.sql | ./mbslave-psql.py
        ./mbslave-remap-schema.py <sql/statistics/CreateIndexes.sql | ./mbslave-psql.py
        ./mbslave-remap-schema.py <sql/caa/CreateIndexes.sql | ./mbslave-psql.py

        ./mbslave-remap-schema.py <sql/CreateViews.sql | ./mbslave-psql.py

 6. Vacuum the newly created database (optional)

        echo 'VACUUM ANALYZE;' | ./mbslave-psql.py

Replication
===========

After the initial database setup, you might want to update the database with the latest data.
The `mbslave sync` script will fetch updates from MusicBrainz and apply it to your local database::

    mbslave sync

In order to update your database regularly, add a cron job like this that runs every hour::

    15 * * * * mbslave sync >>/var/log/mbslave.log

*****************
SQLAlchemy Models
*****************

If you are developing a Python application that needs access to the
`MusicBrainz <https://musicbrainz.org/>`__
`data <https://musicbrainz.org/doc/MusicBrainz_Database>`__, you can use
the ``mbdata.models`` module to get
`SQLAlchemy <http://www.sqlalchemy.org/>`__ models mapped to the
MusicBrainz database tables.

All tables from the MusicBrainz database are mapped, all foreign keys
have one-way relationships set up and some models, where it's essential
to access their related models, have two-way relationships (collections)
set up.

In order to work with the relationships efficiently, you should use the
appropriate kind of `eager
loading <http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html>`__.

Example usage of the models:

.. code:: python

    >>> from sqlalchemy import create_engine
    >>> from sqlalchemy.orm import sessionmaker
    >>> from mbdata.models import Artist
    >>> engine = create_engine('postgresql://musicbrainz:musicbrainz@127.0.0.1/musicbrainz', echo=True)
    >>> Session = sessionmaker(bind=engine)
    >>> session = Session()
    >>> artist = session.query(Artist).filter_by(gid='8970d868-0723-483b-a75b-51088913d3d4').first()
    >>> print artist.name

If you use the models in your own application and want to define foreign
keys from your own models to the MusicBrainz schema, you will need to
let ``mbdata`` know which metadata object to add the MusicBrainz tables
to:

.. code:: python

    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

    # this should be the first place where you import anything from mbdata
    import mbdata.config
    mbdata.config.configure(base_class=Base)

    # now you can import and use the mbdata models
    import mbdata.models

You can also use ``mbdata.config`` to re-map the MusicBrainz schema
names, if your database doesn't follow the original structure:

.. code:: python

    import mbdata.config
    mbdata.config.configure(schema='my_own_mb_schema')

If you need sample MusicBrainz data for your tests, you can use
``mbdata.sample_data``:

.. code:: python

    from mbdata.sample_data import create_sample_data
    create_sample_data(session)

********
HTTP API
********

**Note:** This is very much a work in progress. It is not ready to use
yet. Any help is welcome.

There is also a HTTP API, which you can use to access the MusicBrainz
data using JSON or XML formats over HTTP. This is useful if you want to
abstract away the MusicBrainz PostgreSQL database.

Installation:

.. code:: sh

    virtualenv --system-site-packages e
    . e/bin/activate
    pip install -r requirements.txt
    python setup.py develop

Configuration:

.. code:: sh

    cp settings.py.sample settings.py
    vim settings.py

Start the development server:

.. code:: sh

    MBDATA_API_SETTINGS=`pwd`/settings.py python -m mbdata.api.app

Query the API:

.. code:: sh

    curl 'http://127.0.0.1:5000/v1/artist/get?id=b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d'

For production use, you should use server software like
`uWSGI <http://projects.unbit.it/uwsgi/>`__ and
`nginx <http://nginx.org/>`__ to run the service.

**********
Solr Index
**********

Create a minimal Solr configuration:

.. code:: sh

    ./bin/create_solr_home.py -d /tmp/mbdata_solr

Start Solr:

.. code:: sh

    cd /path/to/solr-4.6.1/example
    java -Dsolr.solr.home=/tmp/mbdata_solr -jar start.jar

***********
Development
***********

Normally you should work against a regular PostgreSQL database with
MusicBrainz data, but for testing purposes, you can use a SQLite
database with small data sub-set used in unit tests. You can create the
database using:

.. code:: sh

    ./bin/create_sample_db.py sample.db

Then you can change your configuration:

.. code:: sh

    DATABASE_URI = 'sqlite:///sample.db'

Running tests:

.. code:: sh

    nosetests -v

If you want to see the SQL queries from a failed test, you can use the
following:

.. code:: sh

    MBDATA_DATABASE_ECHO=1 nosetests -v

Jenkins task that automatically runs the tests after each commit is
`here <http://build.oxygene.sk/job/mbdata/>`__.
