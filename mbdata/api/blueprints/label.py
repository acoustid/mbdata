# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all
from mbdata.models import Label, LabelGIDRedirect
from mbdata.utils import get_something_by_gid
from mbdata.api.utils import get_param, response_ok, response_error
from mbdata.api.includes import LabelIncludes
from mbdata.api.serialize import serialize_label
from mbdata.api.data import load_areas, load_links, query_label
from mbdata.api.search import (
    prepare_page_info,
    prepare_search_options,
    get_search_params,
)
from mbdata.api.errors import (
    INVALID_PARAMETER_ERROR,
    NOT_FOUND_ERROR,
)

blueprint = Blueprint('label', __name__)


def get_label_by_gid(query, gid):
    return get_something_by_gid(query, LabelGIDRedirect, gid)


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=LabelIncludes.parse)

    label = get_label_by_gid(query_label(g.db, include), gid)
    if label is None:
        abort(response_error(NOT_FOUND_ERROR, 'label not found'))

    if include.area:
        load_areas(g.db, [label], include.area)

    if include.relationships:
        load_links(g.db, [label], include.relationships)

    return response_ok(label=serialize_label(label, include))


@blueprint.route('/search')
def handle_search():
    query = get_param('query', type='text')
    include = get_param('include', type='enum+', container=LabelIncludes.parse)

    page = get_search_params()
    options = prepare_search_options(page, fields='name^1.6 sort_name^1.1 alias')
    search_results = g.solr.select(query, fq='kind:label', **options)

    # http://127.0.0.1:8983/solr/musicbrainz/select?q=gender:male&group=true&group.field=kind&group.limit=3&defType=edismax&qf=name&uf=*

    label_ids = []
    scores = {}
    for result in search_results:
        id = int(result['id'].split(':', 1)[1])
        label_ids.append(id)
        scores[id] = result['score']

    labels = query_label(g.db, include).filter(Label.id.in_(label_ids))
    label_by_id = {}
    for label in labels:
        label_by_id[label.id] = label

    if include.areas:
        load_areas(g.db, label_by_id.values(), include.areas)

    data = []
    for id in label_ids:
        data.append({
            'score': scores[id],
            'label': serialize_label(label_by_id[id], include),
        })

    return response_ok(results=data, page_info=prepare_page_info(search_results, page))

