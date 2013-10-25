# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, g, abort
from sqlalchemy.orm import joinedload, subqueryload_all, defer
from mbdata.models import Artist, ArtistGIDRedirect, LinkArtistURL, ArtistTag
from mbdata.utils import defer_everything_but, get_something_by_gid
from mbdata.api.utils import get_param, response_ok, response_error, serialize_partial_date
from mbdata.api.includes import ArtistIncludes
from mbdata.api.serialize import serialize_artist
from mbdata.api.search import (
    parse_page_token,
    prepare_page_info,
    prepare_search_options,
    get_search_params,
)
from mbdata.api.errors import (
    INVALID_PARAMETER_ERROR,
)

blueprint = Blueprint('artist', __name__)


def get_artist_by_gid(query, gid):
    return get_something_by_gid(query, ArtistGIDRedirect, gid)


def get_plain_artist_by_gid_or_error(gid):
    query = g.db.query(Artist).\
        options(*defer_everything_but(Artist, "id", "gid"))
    artist = get_artist_by_gid(query, gid)
    if artist is None:
        abort(response_error(2, 'artist not found'))
    return artist


def query_artist(session):
    query = session.query(Artist).\
        options(subqueryload_all("end_area.type")).\
        options(subqueryload_all("begin_area.type")).\
        options(subqueryload_all("area.type")).\
        options(joinedload("gender")).\
        options(joinedload("type"))

    return query


@blueprint.route('/get')
def handle_get():
    gid = get_param('id', type='uuid', required=True)
    include = get_param('include', type='enum+', container=ArtistIncludes.parse)

    artist = get_artist_by_gid(query_artist(g.db), gid)
    if artist is None:
        abort(response_error(2, 'artist not found'))

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

    artists = query_artist(g.db).filter(Artist.id.in_(artist_ids))
    artist_by_id = {}
    for artist in artists:
        artist_by_id[artist.id] = artist

    data = []
    for id in artist_ids:
        data.append({
            'score': scores[id],
            'artist': serialize_artist(artist_by_id[id], include),
        })

    return response_ok(results=data, page_info=prepare_page_info(search_results, page))


@blueprint.route('/urls')
def handle_urls():
    gid = get_param('id', type='uuid', required=True)
    artist = get_plain_artist_by_gid_or_error(gid)

    query = g.db.query(LinkArtistURL).filter_by(artist=artist).\
        options(joinedload('url', innerjoin=True))
    data = []
    for link in query:
        data.append(link.url.url)

    return response_ok(urls=data)


@blueprint.route('/tags')
def handle_tags():
    gid = get_param('id', type='uuid', required=True)
    artist = get_plain_artist_by_gid_or_error(gid)

    query = g.db.query(ArtistTag).filter_by(artist=artist).\
        options(joinedload('tag', innerjoin=True)).\
        options(defer('last_updated')).\
        options(defer('tag.ref_count'))
    data = []
    for artist_tag in query:
        data.append({
            'name': artist_tag.tag.name,
            'count': artist_tag.count
        })

    return response_ok(tags=data)

