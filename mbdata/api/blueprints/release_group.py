# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload
from mbdata.models import (
    Release,
    ReleaseGroup,
    ReleaseGroupGIDRedirect,
)
from mbdata.utils import get_something_by_gid
from mbdata.api.includes import ReleaseGroupIncludes, ReleaseIncludes
from mbdata.api.data import query_release
from mbdata.api.utils import (
    get_param,
    response_ok,
    response_error,
)
from mbdata.api.errors import NOT_FOUND_ERROR, INCLUDE_DEPENDENCY_ERROR
from mbdata.api.serialize import serialize_release_group, serialize_release

blueprint = Blueprint('release_group', __name__)


def get_release_group_by_gid(query, gid):
    return get_something_by_gid(query, ReleaseGroupGIDRedirect, gid)


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=ReleaseGroupIncludes.parse)

    if include.artist and include.artists:
        abort(response_error(INCLUDE_DEPENDENCY_ERROR, 'include=artist and include=artists are mutually exclusive'))

    query = g.db.query(ReleaseGroup).\
        options(joinedload("type")).\
        options(subqueryload("secondary_types")).\
        options(joinedload("secondary_types.secondary_type", innerjoin=True))

    if include.artist or include.artists:
        query = query.options(joinedload("artist_credit", innerjoin=True))
    if include.artists:
        query = query.\
            options(subqueryload("artist_credit.artists")).\
            options(joinedload("artist_credit.artists.artist", innerjoin=True))

    release_group = get_release_group_by_gid(query, gid)
    if release_group is None:
        abort(response_error(NOT_FOUND_ERROR, 'release group not found'))

    return response_ok(release_group=serialize_release_group(release_group, include))


@blueprint.route('/list_releases')
def handle_list_releases():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=ReleaseIncludes.parse)

    release_group_query = g.db.query(ReleaseGroup.id).filter_by(gid=gid).as_scalar()

    query = query_release(g.db, include).\
        filter(Release.release_group_id == release_group_query).\
        order_by(Release.id).limit(10) # FIXME

    releases_data = []
    for release in query:
        releases_data.append(serialize_release(release, include))

    return response_ok(releases=releases_data)

