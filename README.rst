##########################
MusicBrainz Database Tools
##########################

|pypi badge|

.. |pypi badge| image:: https://badge.fury.io/py/mbdata.svg
    :target: https://badge.fury.io/py/mbdata

********************************
MusicBrainz Database Replication
********************************

This repository now contains a collection of scripts for managing a
replica of the MusicBrainz database. These used to be called "mbslave",
but have been moved to this repository.

The main motivation for these scripts is to be able to customize
your database. If you don't need such customizations, it might be
easier to use the replication tools provided by MusicBrainz itself.

Installation
============

1. You need to have `Python 3.x <https://python.org/>`__ installed on your system.
   Then you can use `pipx <https://pypa.github.io/pipx/>`__ to install this package::

       sudo apt install python3 pipx
       pipx install 'mbdata[replication]'

2. Get an API token on the `MetaBrainz website <https://metabrainz.org/supporters/account-type>`__.

3. Create mbslave.conf by copying and editing `mbslave.conf.default <https://github.com/lalinsky/mbdata/blob/master/mbslave.conf.default>`__::

       curl https://raw.githubusercontent.com/lalinsky/mbdata/master/mbslave.conf.default -o mbslave.conf
       vim mbslave.conf

   By default, the ``mbslave`` script will look for the config file in the current directory.
   If you want it to find it from anywhere, either save it to ``/etc/mbslave.conf`` or
   set the ``MBSLAVE_CONFIG`` environment variable. For example:::

        export MBSLAVE_CONFIG=/usr/local/etc/mbslave.conf

4. Setup the database. If you are starting completely from scratch,
   you can use the following commands to setup a clean database::

       sudo su - postgres
       createuser musicbrainz
       createdb -l C -E UTF-8 -T template0 -O musicbrainz musicbrainz
       psql musicbrainz -c 'CREATE EXTENSION cube;'
       psql musicbrainz -c 'CREATE EXTENSION earthdistance;'

5. Prepare empty schemas for the MusicBrainz database and create the table structure::

       echo 'CREATE SCHEMA musicbrainz;' | mbslave psql -S
       echo 'CREATE SCHEMA statistics;' | mbslave psql -S
       echo 'CREATE SCHEMA cover_art_archive;' | mbslave psql -S
       echo 'CREATE SCHEMA wikidocs;' | mbslave psql -S
       echo 'CREATE SCHEMA documentation;' | mbslave psql -S

       mbslave psql -f CreateCollations.sql
       mbslave psql -f CreateTables.sql
       mbslave psql -f statistics/CreateTables.sql
       mbslave psql -f caa/CreateTables.sql
       mbslave psql -f wikidocs/CreateTables.sql
       mbslave psql -f documentation/CreateTables.sql

6. Download the MusicBrainz database dump files from
   http://ftp.musicbrainz.org/pub/musicbrainz/data/fullexport/

7. Import the data dumps, for example::

       mbslave import mbdump.tar.bz2 mbdump-derived.tar.bz2

8. Setup primary keys, indexes and views::

       mbslave psql -f CreatePrimaryKeys.sql
       mbslave psql -f statistics/CreatePrimaryKeys.sql
       mbslave psql -f caa/CreatePrimaryKeys.sql
       mbslave psql -f wikidocs/CreatePrimaryKeys.sql
       mbslave psql -f documentation/CreatePrimaryKeys.sql

       mbslave psql -f CreateIndexes.sql
       mbslave psql -f CreateSlaveIndexes.sql
       mbslave psql -f statistics/CreateIndexes.sql
       mbslave psql -f caa/CreateIndexes.sql

       mbslave psql -f CreateFunctions.sql
       mbslave psql -f CreateViews.sql

9. Vacuum the newly created database (optional)::

       echo 'VACUUM ANALYZE;' | mbslave psql

Replication
===========

After the initial database setup, you might want to update the database with the latest data.
The `mbslave sync` script will fetch updates from MusicBrainz and apply it to your local database::

    mbslave sync

In order to update your database regularly, add a cron job like this that runs every hour::

    15 * * * * mbslave sync >>/var/log/mbslave.log

Schema Upgrade
==============

When the MusicBrainz database schema changes, the replication will stop working.
This is usually announced on the `MusicBrainz blog <http://blog.musicbrainz.org/>`__.
When it happens, you need to upgrade the database.

Release 2022-05-16 (27)
~~~~~~~~~~~~~~~~~~~~~~~

Run the upgrade scripts::

    mbslave psql -f updates/schema-change/27.mirror.sql
    echo 'UPDATE replication_control SET current_schema_sequence = 27;' | mbslave psql

Release 2021-05-17 (26)
~~~~~~~~~~~~~~~~~~~~~~~

Run the upgrade scripts::

    mbslave psql -f updates/schema-change/26.slave.sql
    echo 'UPDATE replication_control SET current_schema_sequence = 26;' | mbslave psql

2020-05-18 Upgrade to PostgreSQL 12
-----------------------------------

These steps are recommended even if you were already running on Postgres 12 before MusicBrainz
moved to make PostgreSQL 12 the minimal supported version.

Run the pre-upgrade script::

   mbslave psql -f updates/20200518-pg12-before-upgrade.sql

If not already on PostgreSQL 12, upgrade your cluster now (depending on your OS, using
`pg_upgradecluster` or `pg_upgrade`)

After upgrading, or if already on PostgreSQL 12, run::

   mbslave psql -f updates/20200518-pg12-after-upgrade.sql

Release 2019-05-14 (25)
~~~~~~~~~~~~~~~~~~~~~~~

Run the upgrade scripts::

    mbslave psql -f updates/schema-change/25.slave.sql
    echo 'UPDATE replication_control SET current_schema_sequence = 25;' | mbslave psql

Release 2017-05-25 (24)
~~~~~~~~~~~~~~~~~~~~~~~

Run the upgrade scripts::

    mbslave psql -f updates/schema-change/24.slave.sql
    echo 'UPDATE replication_control SET current_schema_sequence = 24;' | mbslave psql

Tips and Tricks
===============

Single Database Schema
~~~~~~~~~~~~~~~~~~~~~~

MusicBrainz uses a number of schemas by default. If you are embedding the MusicBrainz database into
an existing database for your application, it's convenient to merge them all into a single schema.
That can be done by changing your config like this::

    [schemas]
    musicbrainz=musicbrainz
    statistics=musicbrainz
    cover_art_archive=musicbrainz
    wikidocs=musicbrainz
    documentation=musicbrainz

After this, you only need to create the "musicbrainz" schema and import all the tables there.

Full Import Schema Upgrade
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the schema mapping feature to do zero-downtime upgrade of the database with full
data import. You can temporarily map all schemas to e.g. "musicbrainz_NEW", import your new
database there and then rename it::

    echo 'BEGIN; ALTER SCHEMA musicbrainz RENAME TO musicbrainz_OLD; ALTER SCHEMA musicbrainz_NEW RENAME TO musicbrainz; COMMIT;' | mbslave psql -S

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
