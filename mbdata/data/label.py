# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all, defer
from mbdata.models import (
    Label,
)
from mbdata.api.data import (
    query_label,
    load_areas,
    load_links,
)
from mbdata.api.serialize import (
    serialize_label,
)


def get_labels_by_ids(db, ids, include):
    if not ids:
        return {}

    labels = query_label(db, include).filter(Label.id.in_(ids)).all()

    if include.relationships:
        load_links(db, labels, include.relationships)

    results = {}
    for label in labels:
        results[label.id] = serialize_label(label, include)
    return results

