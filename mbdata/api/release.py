# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, request, g, abort
from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all, defer
from mbdata.models import (
    Release,
    ReleaseGIDRedirect,
    ReleaseGroupSecondaryTypeJoin,
    Medium,
    Track,
)
from mbdata.utils import defer_everything_but, get_something_by_gid
from mbdata.api.utils import get_param, response_ok, response_error, serialize_partial_date
from mbdata.api.errors import NOT_FOUND_ERROR

blueprint = Blueprint('release', __name__)


def get_release_by_gid(query, gid):
    return get_something_by_gid(query, ReleaseGIDRedirect, gid)


def get_plain_release_by_gid_or_error(gid):
    query = g.db.query(Release).\
        options(*defer_everything_but(Release, "id", "gid"))
    release = get_release_by_gid(query, gid)
    if release is None:
        abort(response_error(2, 'release not found'))
    return release


@blueprint.route('/details')
def release_details():
    gid = get_param('id', type='uuid', required=True)

    query = g.db.query(Release).\
        options(joinedload("status")).\
        options(joinedload("packaging")).\
        options(joinedload("language")).\
        options(joinedload("script")).\
        options(joinedload("artist_credit", innerjoin=True)).\
        options(joinedload("release_group", innerjoin=True)).\
        options(joinedload("release_group.type")).\
        options(subqueryload("release_group.secondary_types")).\
        options(joinedload("release_group.secondary_types.secondary_type", innerjoin=True)).\
        options(subqueryload("mediums")).\
        options(joinedload("mediums.format")).\
        options(subqueryload("mediums.tracks")).\
        options(joinedload("mediums.tracks.artist_credit", innerjoin=True))

    release = get_release_by_gid(query, gid)
    if release is None:
        abort(response_error(NOT_FOUND_ERROR, 'release not found'))

    data = {
        'id': release.gid,
        'name': release.name,
        'release_group': {
            'id': release.release_group.gid,
            'name': release.release_group.name,
        }
    }

    if release.release_group.type:
        data['release_group']['type'] = release.release_group.type.name

    if release.release_group.secondary_types:
        data['release_group']['secondary_types'] = []
        for type in release.release_group.secondary_type:
            data['release_group']['secondary_types'].append(type.secondary_type.name)

    if release.status:
        data['status'] = release.status.name

    if release.packaging:
        data['packaging'] = release.packaging.name

    if release.language:
        data['language'] = release.language.name

    if release.script:
        data['script'] = release.script.name

    data['mediums'] = []
    for medium in release.mediums:
        medium_data ={
            'position': medium.position,
            'tracks': [],
        }
        if medium.name:
            medium_data['name'] = medium.name
        if medium.format:
            medium_data['format'] = medium.format.name
        for track in medium.tracks:
            track_data = {
                'id': track.gid,
                'name': track.name,
                'position': track.position,
            }
            if str(track.position) != track.number:
                track_data['number'] = track.number
            if track.length:
                track_data['length'] = track.length / 1000.0
            medium_data['tracks'].append(track_data)
        data['mediums'].append(medium_data)

    return response_ok(release=data)

