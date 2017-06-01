# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

NO_SCHEMAS = {
    'musicbrainz': None,
    'cover_art_archive': None,
    'wikidocs': None,
    'statistics': None,
    'documentation': None,
}

SINGLE_MUSICBRAINZ_SCHEMA = {
    'musicbrainz': 'musicbrainz',
    'cover_art_archive': 'musicbrainz',
    'wikidocs': 'musicbrainz',
    'statistics': 'musicbrainz',
    'documentation': 'musicbrainz',
}


def patch_model_schemas(mapping):
    """Update mbdata.models to use different schema names

    The function accepts a dictionary with schema name mapping
    and updates the schema for all MusicBrainz tables.

    If you want to use the default schema:

    >>> patch_model_schemas(NO_SCHEMAS)

    If you have just one 'musicbrainz' schema:

    >>> patch_model_schemas(SINGLE_MUSICBRAINZ_SCHEMA)

    """
    from mbdata.models import Base

    for table in Base.metadata.sorted_tables:
        if table.schema is None:
            continue
        table.schema = mapping.get(table.schema, table.schema)


def get_something_by_gid(query, redirect_model, gid):
    artist = query.filter_by(gid=gid).first()
    if artist is None:
        subquery = query.session.query(redirect_model.redirect_id).\
            filter_by(gid=gid)
        artist = query.filter(redirect_model.redirect.property.primaryjoin.left.in_(subquery)).first()
    return artist

