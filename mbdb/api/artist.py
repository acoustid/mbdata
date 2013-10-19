from flask import Blueprint, request, g, jsonify, abort
from sqlalchemy.orm import joinedload, subqueryload_all, defer
from mbdb.models import Artist, ArtistGIDRedirect, Area, LinkArtistURL, ArtistTag
from mbdb.utils import defer_everything_but
from mbdb.api.utils import get_param, response_ok, response_error, serialize_partial_date

blueprint = Blueprint('artist', __name__)


def get_artist_by_gid(query, gid):
    artist = query.filter_by(gid=gid).first()
    if artist is None:
        subquery = g.db.query(ArtistGIDRedirect.new_id_id).filter_by(gid=gid)
        artist = query.filter(Artist.id.in_(subquery)).first()
    return artist


def get_plain_artist_by_gid_or_error(gid):
    query = g.db.query(Artist).\
        options(*defer_everything_but(Artist, "id", "gid"))
    artist = get_artist_by_gid(query, gid)
    if artist is None:
        abort(response_error(2, 'artist not found'))
    return artist


@blueprint.route('/profile')
def artist_profile():
    gid = get_param('id', type='uuid', required=True)

    query = g.db.query(Artist).\
        options(subqueryload_all("end_area.type")).\
        options(subqueryload_all("begin_area.type")).\
        options(subqueryload_all("area.type")).\
        options(joinedload("gender")).\
        options(joinedload("type"))

    artist = get_artist_by_gid(query, gid)
    if artist is None:
        abort(response_error(2, 'artist not found'))

    data = {
        'id': artist.gid,
        'name': artist.name,
        'sort_name': artist.sort_name,
    }

    serialize_partial_date(data, 'begin_date', artist.begin_date)
    serialize_partial_date(data, 'end_date', artist.end_date)

    if artist.ended:
        data['ended'] = True

    if artist.type:
        data['type'] = artist.type.name

    if artist.gender:
        data['gender'] = artist.gender.name

    if artist.area:
        data['area'] = artist.area.name

    if artist.begin_area:
        data['begin_area'] = artist.begin_area.name

    if artist.end_area:
        data['end_area'] = artist.end_area.name

    return response_ok(artist=data)


@blueprint.route('/urls')
def artist_urls():
    gid = get_param('id', type='uuid', required=True)
    artist = get_plain_artist_by_gid_or_error(gid)

    query = g.db.query(LinkArtistURL).filter_by(artist=artist).\
        options(joinedload('url', innerjoin=True))
    data = []
    for link in query:
        data.append(link.url.url)

    return response_ok(urls=data)


@blueprint.route('/tags')
def artist_tags():
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

