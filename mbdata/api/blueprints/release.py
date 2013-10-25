# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload
from mbdata.models import (
    Release,
    ReleaseGIDRedirect,
)
from mbdata.utils import get_something_by_gid
from mbdata.api.includes import ReleaseIncludes
from mbdata.api.utils import (
    get_param,
    response_ok,
    response_error,
    serialize_partial_date,
)
from mbdata.api.errors import NOT_FOUND_ERROR, INCLUDE_DEPENDENCY_ERROR
from mbdata.api.serialize import serialize_release

blueprint = Blueprint('release', __name__)


def get_release_by_gid(query, gid):
    return get_something_by_gid(query, ReleaseGIDRedirect, gid)


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=ReleaseIncludes.parse)

    if include.artist_names and include.artist_credits:
        abort(response_error(INCLUDE_DEPENDENCY_ERROR, 'include=artist_names and include=artist_credits are mutually exclusive'))

    query = g.db.query(Release).\
        options(joinedload("status")).\
        options(joinedload("packaging")).\
        options(joinedload("language")).\
        options(joinedload("script"))

    if include.artist_names or include.artist_credits:
        query = query.options(joinedload("artist_credit", innerjoin=True))
    if include.artist_credits:
        query = query.\
            options(subqueryload("artist_credit.artists")).\
            options(joinedload("artist_credit.artists.artist", innerjoin=True))

    if include.release_group:
        query = query.\
            options(joinedload("release_group.type")).\
            options(subqueryload("release_group.secondary_types")).\
            options(joinedload("release_group.secondary_types.secondary_type", innerjoin=True))

        if include.release_group.artist_names or include.release_group.artist_credits:
            query = query.options(joinedload("release_group.artist_credit", innerjoin=True))
        if include.release_group.artist_credits:
            query = query.\
                options(subqueryload("release_group.artist_credit.artists")).\
                options(joinedload("release_group.artist_credit.artists.artist", innerjoin=True))

    if include.mediums:
        query = query.options(joinedload("mediums.format"))

        if include.mediums.tracks:
            query = query.options(subqueryload("mediums.tracks"))

            if include.mediums.tracks.artist_names or include.mediums.tracks.artist_credits:
                query = query.options(joinedload("mediums.tracks.artist_credit", innerjoin=True))
            if include.mediums.tracks.artist_credits:
                query = query.\
                    options(subqueryload("mediums.tracks.artist_credit.artists")).\
                    options(joinedload("mediums.tracks.artist_credit.artists.artist", innerjoin=True))

    release = get_release_by_gid(query, gid)
    if release is None:
        abort(response_error(NOT_FOUND_ERROR, 'release not found'))

    return response_ok(release=serialize_release(release, include))

