# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all, defer
from mbdata.models import (
    Artist,
)
from mbdata.api.data import (
    query_artist,
    load_areas,
    load_links,
)
from mbdata.api.serialize import (
    serialize_artist,
)


def get_artists_by_ids(db, ids, include):
    if not ids:
        return {}

    artists = query_artist(db, include).filter(Artist.id.in_(ids)).all()

    if include.areas:
        load_areas(db, artists, include.areas)

    if include.relationships:
        load_links(db, artists, include.relationships)

    results = {}
    for artist in artists:
        results[artist.id] = serialize_artist(artist, include)
    return results

