from nose.tools import *
from sqlalchemy.orm import noload
from mbdata.models import Artist, Work
from mbdata.api.data import load_areas, load_links
from mbdata.api.includes import AreaIncludes, RelationshipsIncludes
from mbdata.api.tests import with_database


@with_database
def test_load_areas_simple(db):
    artist = db.query(Artist).filter_by(gid='95db1c7c-21b8-4956-82ad-20217cd5d395').\
        options(noload('area')).options(noload('begin_area')).one()
    load_areas(db, [artist], AreaIncludes.parse([]))

    assert_true(artist.area)
    assert_equal(artist.area.name, 'Canada')
    assert_false(hasattr(artist.area, 'part_of'))

    assert_true(artist.begin_area)
    assert_equal(artist.begin_area.name, 'New York')
    assert_false(hasattr(artist.begin_area, 'part_of'))

    assert_true(artist.end_area)
    assert_equal(artist.end_area.name, 'Montreal')
    assert_false(hasattr(artist.end_area, 'part_of'))


@with_database
def test_load_areas_recursive(db):
    artist = db.query(Artist).filter_by(gid='95db1c7c-21b8-4956-82ad-20217cd5d395').\
        options(noload('area')).options(noload('begin_area')).one()
    load_areas(db, [artist], AreaIncludes.parse(['part_of']))

    assert_true(artist.area)
    assert_equal(artist.area.name, 'Canada')
    assert_false(artist.area.part_of)

    assert_true(artist.begin_area)
    assert_equal(artist.begin_area.name, 'New York')
    assert_true(artist.begin_area.part_of)
    assert_equal(artist.begin_area.part_of.name, 'United States')
    assert_false(artist.begin_area.part_of.part_of)

    assert_true(artist.end_area)
    assert_equal(artist.end_area.name, 'Montreal')
    assert_true(artist.end_area.part_of)
    assert_equal(artist.end_area.part_of.name, 'Quebec')
    assert_true(artist.end_area.part_of.part_of)
    assert_equal(artist.end_area.part_of.part_of.name, 'Canada')
    assert_false(artist.end_area.part_of.part_of.part_of)


@with_database
def test_load_links(db):
    work = db.query(Work).filter_by(gid='e02ccc5b-d39f-31d2-aaf5-b56ad67e4ffe').one()
    load_links(db, [work], RelationshipsIncludes.parse(['artist']))

    assert_equals(len(work.artist_links), 2)

    link = work.artist_links[0]
    assert_equals(link.link.link_type.name, 'composer')
    assert_equals(link.artist.name, 'Richard Melville Hall')

    link = work.artist_links[1]
    assert_equals(link.link.link_type.name, 'lyricist')
    assert_equals(link.artist.name, 'Richard Melville Hall')

