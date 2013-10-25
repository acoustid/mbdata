# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload
from mbdata.models import (
    Work,
    WorkGIDRedirect,
)
from mbdata.utils import get_something_by_gid
from mbdata.api.includes import WorkIncludes
from mbdata.api.utils import (
    get_param,
    response_ok,
    response_error,
)
from mbdata.api.errors import NOT_FOUND_ERROR, INCLUDE_DEPENDENCY_ERROR
from mbdata.api.serialize import serialize_work, serialize_release

blueprint = Blueprint('work', __name__)


def get_work_by_gid(query, gid):
    return get_something_by_gid(query, WorkGIDRedirect, gid)


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=WorkIncludes.parse)

    query = g.db.query(Work)

    work = get_work_by_gid(query, gid)
    if work is None:
        abort(response_error(NOT_FOUND_ERROR, 'work not found'))

    work_data = serialize_work(work, include)

    return response_ok(work=work_data)

