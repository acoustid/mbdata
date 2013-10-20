# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Blueprint, request, g, abort
from sqlalchemy.orm import joinedload, subqueryload, subqueryload_all, defer
from mbdata.models import (
    Release,
    ReleaseGIDRedirect,
    ReleaseGroupSecondaryTypeJoin,
    Medium,
    Track,
)
from mbdata.utils import defer_everything_but, get_something_by_gid
from mbdata.api.utils import (
    get_param,
    response_ok,
    response_error,
    serialize_partial_date,
    make_includes,
)
from mbdata.api.errors import NOT_FOUND_ERROR, INCLUDE_DEPENDENCY_ERROR

blueprint = Blueprint('release', __name__)


def get_release_by_gid(query, gid):
    return get_something_by_gid(query, ReleaseGIDRedirect, gid)


def get_plain_release_by_gid_or_error(gid):
    query = g.db.query(Release).\
        options(*defer_everything_but(Release, "id", "gid"))
    release = get_release_by_gid(query, gid)
    if release is None:
        abort(response_error(2, 'release not found'))
    return release


def serialize_artist_credit(artist_credit):
    data = []
    for artist_credit_name in artist_credit.artists:
        artist_credit_data = {
            'id': artist_credit_name.artist.gid,
            'name': artist_credit_name.artist.name,
        }

        if artist_credit_name.name != artist_credit_name.artist.name:
            artist_credit_name['credited_name'] = artist_credit_name.name

        if artist_credit_name.join_phrase:
            artist_credit_data['join_phrase'] = artist_credit_name.join_phrase

        data.append(artist_credit_data)

    return data


def serialize_track(track, include):
    data = {
        'id': track.gid,
        'name': track.name,
        'position': track.position,
    }

    if str(track.position) != track.number:
        data['number'] = track.number

    if track.length:
        data['length'] = track.length / 1000.0

    if include.artist_names:
        data['artist'] = track.artist_credit.name
    elif include.artist_credits:
        data['artists'] = serialize_artist_credit(track.artist_credit)

    return data


def serialize_medium(medium, include):
    data = {
        'position': medium.position,
    }

    if medium.name:
        data['name'] = medium.name

    if medium.format:
        data['format'] = medium.format.name

    if include.tracks:
        tracks_data = []
        for track in medium.tracks:
            tracks_data.append(serialize_track(track, include))
        data['tracks'] = tracks_data
    else:
        data['track_count'] = medium.track_count

    return data


def serialize_release_group(release_group, include):
    data = {
        'id': release_group.gid,
        'name': release_group.name,
    }

    if release_group.type:
        data['type'] = release_group.type.name

    if release_group.secondary_types:
        data['secondary_types'] = []
        for type in release_group.secondary_type:
            data['secondary_types'].append(type.secondary_type.name)

    if include.artist_names:
        data['artist'] = release_group.artist_credit.name
    elif include.artist_credits:
        data['artists'] = serialize_artist_credit(release_group.artist_credit)

    return data


def serialize_release(release, include):
    data = {
        'id': release.gid,
        'name': release.name,
    }

    if release.status:
        data['status'] = release.status.name

    if release.packaging:
        data['packaging'] = release.packaging.name

    if release.language:
        data['language'] = release.language.name

    if release.script:
        data['script'] = release.script.name

    if include.artist_names:
        data['artist'] = release.artist_credit.name
    elif include.artist_credits:
        data['artists'] = serialize_artist_credit(release.artist_credit)

    if include.release_group:
        data['release_group'] = serialize_release_group(release.release_group, include)

    if include.mediums:
        mediums_data = []
        for medium in release.mediums:
            mediums_data.append(serialize_medium(medium, include))
        data['mediums'] = mediums_data

    return data


@blueprint.route('/details')
def release_details():
    gid = get_param('id', type='uuid', required=True)

    includes_class = make_includes('mediums', 'tracks', 'release_group', 'artist_names', 'artist_credits')
    include = get_param('include', type='enum+', container=includes_class)

    if include.artist_names and include.artist_credits:
        abort(response_error(INCLUDE_DEPENDENCY_ERROR, 'include=artist_names and include=artist_credits are mutually exclusive'))

    query = g.db.query(Release).\
        options(joinedload("status")).\
        options(joinedload("packaging")).\
        options(joinedload("language")).\
        options(joinedload("script"))

    if include.artist_names or include.artist_credits:
        query = query.options(joinedload("artist_credit", innerjoin=True))
    if include.artist_credits:
        query = query.\
            options(subqueryload("artist_credit.artists")).\
            options(joinedload("artist_credit.artists.artist", innerjoin=True))

    if include.release_group:
        query = query.\
            options(joinedload("release_group.type")).\
            options(subqueryload("release_group.secondary_types")).\
            options(joinedload("release_group.secondary_types.secondary_type", innerjoin=True))

        if include.artist_names or include.artist_credits:
            query = query.options(joinedload("release_group.artist_credit", innerjoin=True))
        if include.artist_credits:
            query = query.\
                options(subqueryload("release_group.artist_credit.artists")).\
                options(joinedload("release_group.artist_credit.artists.artist", innerjoin=True))

    if include.mediums:
        query = query.options(joinedload("mediums.format"))

    if include.tracks:
        if not include.mediums:
            abort(response_error(INCLUDE_DEPENDENCY_ERROR, 'include=mediums requires include=tracks'))

        query = query.options(subqueryload("mediums.tracks"))

        if include.artist_names or include.artist_credits:
            query = query.options(joinedload("mediums.tracks.artist_credit", innerjoin=True))
        if include.artist_credits:
            query = query.\
                options(subqueryload("mediums.tracks.artist_credit.artists")).\
                options(joinedload("mediums.tracks.artist_credit.artists.artist", innerjoin=True))

    release = get_release_by_gid(query, gid)
    if release is None:
        abort(response_error(NOT_FOUND_ERROR, 'release not found'))

    return response_ok(release=serialize_release(release, include))

