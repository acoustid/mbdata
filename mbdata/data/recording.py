# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all, defer
from mbdata.models import (
    Recording,
)
from mbdata.api.data import (
    query_recording,
    load_links,
)
from mbdata.api.serialize import (
    serialize_recording,
)


def get_recordings_by_ids(db, ids, include):
    if not ids:
        return {}

    recordings = query_recording(db, include).filter(Recording.id.in_(ids)).all()

    if include.relationships:
        load_links(db, recordings, include.relationships)

    results = {}
    for recording in recordings:
        results[recording.id] = serialize_recording(recording, include)
    return results

