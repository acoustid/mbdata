# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, request, g, abort
from sqlalchemy.orm import joinedload, joinedload_all, subqueryload_all, defer
from mbdata.models import Place, PlaceGIDRedirect, LinkPlaceURL
from mbdata.utils import defer_everything_but, get_something_by_gid
from mbdata.api.utils import get_param, response_ok, response_error, serialize_partial_date
from mbdata.api.errors import NOT_FOUND_ERROR

blueprint = Blueprint('place', __name__)


def get_place_by_gid(query, gid):
    return get_something_by_gid(query, PlaceGIDRedirect, gid)


@blueprint.route('/details')
def place_details():
    gid = get_param('id', type='uuid', required=True)
    include = set(['urls'])

    query = g.db.query(Place).\
        options(joinedload("type"))

    place = get_place_by_gid(query, gid)
    if place is None:
        abort(response_error(NOT_FOUND_ERROR, 'place not found'))

    context = {}

    data = {
        'id': place.gid,
        'name': place.name,
    }

    serialize_partial_date(data, 'begin_date', place.begin_date)
    serialize_partial_date(data, 'end_date', place.end_date)

    if place.ended:
        data['ended'] = True

    if place.type:
        data['type'] = place.type.name

    if place.coordinates:
        data['coordinates'] = {
            'latitude': place.coordinates[0],
            'longitude': place.coordinates[1],
        }

    context['place'] = data

    if 'urls' in include:
        query = g.db.query(LinkPlaceURL).filter_by(place=place).\
            options(joinedload('url', innerjoin=True)).\
            options(joinedload('link', innerjoin=True)).\
            options(joinedload('link.link_type', innerjoin=True))

        urls = []
        for link in query:
            urls.append({
                'url': link.url.url,
                'type': link.link.link_type.name,
            })

        context['urls'] = urls

    return response_ok(**context)

