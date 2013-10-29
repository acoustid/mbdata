# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload
from mbdata.models import Place, PlaceGIDRedirect, LinkPlaceURL
from mbdata.utils import get_something_by_gid
from mbdata.api.utils import get_param, response_ok, response_error
from mbdata.api.includes import PlaceIncludes
from mbdata.api.serialize import serialize_place
from mbdata.api.data import load_areas
from mbdata.api.errors import NOT_FOUND_ERROR

blueprint = Blueprint('place', __name__)


def get_place_by_gid(query, gid):
    return get_something_by_gid(query, PlaceGIDRedirect, gid)


def query_place(db, include):
    return g.db.query(Place).options(joinedload("type"))


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=PlaceIncludes.parse)

    place = get_place_by_gid(query_place(g.db, include), gid)
    if place is None:
        abort(response_error(NOT_FOUND_ERROR, 'place not found'))

    if include.area:
        load_areas(g.db, [place], include.area)

    return response_ok(place=serialize_place(place, include))

