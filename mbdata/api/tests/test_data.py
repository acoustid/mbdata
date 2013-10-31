from nose.tools import *
from sqlalchemy.orm import noload
from mbdata.models import Artist
from mbdata.api.data import load_areas
from mbdata.api.includes import AreaIncludes
from mbdata.api.tests import with_database


@with_database
def test_load_areas_simple(db):
    artist = db.query(Artist).filter_by(gid='95db1c7c-21b8-4956-82ad-20217cd5d395').\
        options(noload('area')).options(noload('begin_area')).one()
    load_areas(db, [artist], AreaIncludes.parse([]))

    assert_true(artist.area)
    assert_equal(artist.area.name, 'United States')
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
    assert_equal(artist.area.name, 'United States')
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

