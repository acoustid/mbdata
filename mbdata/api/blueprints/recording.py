# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload
from mbdata.models import (
    Recording,
    RecordingGIDRedirect,
)
from mbdata.utils import get_something_by_gid
from mbdata.api.utils import (
    get_param,
    response_ok,
    response_error,
    make_includes,
)
from mbdata.api.errors import NOT_FOUND_ERROR, INCLUDE_DEPENDENCY_ERROR
from mbdata.api.serialize import serialize_recording, serialize_release

blueprint = Blueprint('recording', __name__)


def get_recording_by_gid(query, gid):
    return get_something_by_gid(query, RecordingGIDRedirect, gid)


@blueprint.route('/details')
def details():
    gid = get_param('id', type='uuid', required=True)

    includes_class = make_includes('artist_names', 'artist_credits', 'isrcs')
    include = get_param('include', type='enum+', container=includes_class)

    if include.artist_names and include.artist_credits:
        abort(response_error(INCLUDE_DEPENDENCY_ERROR, 'include=artist_names and include=artist_credits are mutually exclusive'))

    query = g.db.query(Recording)

    if include.artist_names or include.artist_credits:
        query = query.options(joinedload("artist_credit", innerjoin=True))
    if include.artist_credits:
        query = query.\
            options(subqueryload("artist_credit.artists")).\
            options(joinedload("artist_credit.artists.artist", innerjoin=True))

    recording = get_recording_by_gid(query, gid)
    if recording is None:
        abort(response_error(NOT_FOUND_ERROR, 'recording not found'))

    return response_ok(recording=serialize_recording(recording, include))

