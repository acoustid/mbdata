# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from mbdata.models import (
    Release,
    ReleaseGIDRedirect,
)
from mbdata.utils import get_something_by_gid
from mbdata.api.data import query_release, load_links
from mbdata.api.includes import ReleaseIncludes
from mbdata.api.utils import (
    get_param,
    response_ok,
    response_error,
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

    if include.artist and include.artists:
        abort(response_error(INCLUDE_DEPENDENCY_ERROR, 'include=artist and include=artists are mutually exclusive'))

    release = get_release_by_gid(query_release(g.db, include), gid)
    if release is None:
        abort(response_error(NOT_FOUND_ERROR, 'release not found'))

    if include.relationships:
        load_links(g.db, [release], include.relationships)

    return response_ok(release=serialize_release(release, include))

