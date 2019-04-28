# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload
from mbdata.models import (
    Recording,
    RecordingGIDRedirect,
)
from mbdata.utils import get_something_by_gid
from mbdata.api.data import load_links, query_recording
from mbdata.api.includes import RecordingIncludes
from mbdata.api.utils import (
    get_param,
    response_ok,
    response_error,
)
from mbdata.api.errors import NOT_FOUND_ERROR, INCLUDE_DEPENDENCY_ERROR
from mbdata.api.serialize import serialize_recording

blueprint = Blueprint('recording', __name__)


def get_recording_by_gid(query, gid):
    return get_something_by_gid(query, RecordingGIDRedirect, gid)


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=RecordingIncludes.parse)

    if include.artist and include.artists:
        abort(response_error(INCLUDE_DEPENDENCY_ERROR, 'include=artist and include=artists are mutually exclusive'))

    recording = get_recording_by_gid(query_recording(g.db, include), gid)
    if recording is None:
        abort(response_error(NOT_FOUND_ERROR, 'recording not found'))

    if include.relationships:
        load_links(g.db, [recording], include.relationships)

    return response_ok(recording=serialize_recording(recording, include))

