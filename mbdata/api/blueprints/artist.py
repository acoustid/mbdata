# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all, defer, load_only
from mbdata.models import (
    Artist,
    ArtistCreditName,
    ArtistGIDRedirect,
    Release,
    ReleaseGroup,
)
from mbdata.utils import get_something_by_gid
from mbdata.api.utils import get_param, response_ok, response_error
from mbdata.api.includes import ArtistIncludes, ReleaseIncludes
from mbdata.api.serialize import (
    serialize_artist,
    serialize_release,
    serialize_release_group,
)
from mbdata.api.data import load_areas, load_links, query_artist, query_release, query_release_group
from mbdata.api.search import (
    parse_page_token,
    prepare_page_info,
    prepare_search_options,
    get_search_params,
)
from mbdata.api.errors import (
    INVALID_PARAMETER_ERROR,
    NOT_FOUND_ERROR,
)

blueprint = Blueprint('artist', __name__)


def get_artist_by_gid(query, gid):
    return get_something_by_gid(query, ArtistGIDRedirect, gid)


def get_plain_artist_by_gid_or_error(gid):
    query = g.db.query(Artist).\
        options(load_only("id", "gid"))
    artist = get_artist_by_gid(query, gid)
    if artist is None:
        abort(response_error(NOT_FOUND_ERROR, 'artist not found'))
    return artist


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=ArtistIncludes.parse)

    artist = get_artist_by_gid(query_artist(g.db, include), gid)
    if artist is None:
        abort(response_error(NOT_FOUND_ERROR, 'artist not found'))

    if include.areas:
        load_areas(g.db, [artist], include.areas)

    if include.relationships:
        load_links(g.db, [artist], include.relationships)

    return response_ok(artist=serialize_artist(artist, include))


@blueprint.route('/search')
def handle_search():
    query = get_param('query', type='text')
    include = get_param('include', type='enum+', container=ArtistIncludes.parse)

    page = get_search_params()
    options = prepare_search_options(page, fields='name^1.6 sort_name^1.1 alias')
    search_results = g.solr.select(query, fq='kind:artist', **options)

    # http://127.0.0.1:8983/solr/musicbrainz/select?q=gender:male&group=true&group.field=kind&group.limit=3&defType=edismax&qf=name&uf=*

    artist_ids = []
    scores = {}
    for result in search_results:
        id = int(result['id'].split(':', 1)[1])
        artist_ids.append(id)
        scores[id] = result['score']

    artists = query_artist(g.db, include).filter(Artist.id.in_(artist_ids))
    artist_by_id = {}
    for artist in artists:
        artist_by_id[artist.id] = artist

    if include.areas:
        load_areas(g.db, artist_by_id.values(), include.areas)

    data = []
    for id in artist_ids:
        data.append({
            'score': scores[id],
            'artist': serialize_artist(artist_by_id[id], include),
        })

    return response_ok(results=data, page_info=prepare_page_info(search_results, page))


@blueprint.route('/list_releases')
def handle_list_releases():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=ReleaseIncludes.parse)

    artist = get_plain_artist_by_gid_or_error(gid)
    artist_credits_query = g.db.query(ArtistCreditName.artist_credit_id).\
        filter_by(artist_id=artist.id)

    query = query_release(g.db, include).\
        filter(Release.artist_credit_id.in_(artist_credits_query)).\
        order_by(Release.id).limit(10)  # FIXME

    releases_data = []
    for release in query:
        releases_data.append(serialize_release(release, include))

    return response_ok(releases=releases_data)


@blueprint.route('/list_release_groups')
def handle_list_release_groups():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=ReleaseIncludes.parse)

    artist = get_plain_artist_by_gid_or_error(gid)
    artist_credits_query = g.db.query(ArtistCreditName.artist_credit_id).\
        filter_by(artist_id=artist.id)

    query = query_release_group(g.db, include).\
        filter(ReleaseGroup.artist_credit_id.in_(artist_credits_query)).\
        order_by(ReleaseGroup.id).limit(10)  # FIXME

    release_groups_data = []
    for release_group in query:
        release_groups_data.append(serialize_release_group(release_group, include))

    return response_ok(release_groups=release_groups_data)

