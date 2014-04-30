# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all, defer
from mbdata.models import (
    ReleaseGroup,
)
from mbdata.api.data import (
    query_release_group,
    load_links,
)
from mbdata.api.serialize import (
    serialize_release_group,
)


def get_release_groups_by_ids(db, ids, include):
    if not ids:
        return {}

    release_groups = query_release_group(db, include).filter(ReleaseGroup.id.in_(ids)).all()

    if include.relationships:
        load_links(db, release_groups, include.relationships)

    results = {}
    for release_group in release_groups:
        results[release_group.id] = serialize_release_group(release_group, include)
    return results

