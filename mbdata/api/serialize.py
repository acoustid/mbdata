# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from mbdata.api.utils import serialize_partial_date


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


def serialize_work(work, include):
    data = {
        'id': work.gid,
        'name': work.name,
    }

    if include.iswcs:
        data['iswcs'] = [iswc.iswc for iswc in work.iswcs]

    return data


def serialize_recording(recording, include):
    data = {
        'id': recording.gid,
        'name': recording.name,
    }

    if recording.length:
        data['length'] = recording.length / 1000.0

    if include.artist_names:
        data['artist'] = recording.artist_credit.name
    elif include.artist_credits:
        data['artists'] = serialize_artist_credit(recording.artist_credit)

    if include.isrcs:
        data['isrcs'] = [isrc.isrc for isrc in recording.isrcs]

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


def serialize_release(release, include, no_release_group=False, no_mediums=False):
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

    if not no_release_group and include.release_group:
        data['release_group'] = serialize_release_group(release.release_group, include)

    if not no_mediums and include.mediums:
        mediums_data = []
        for medium in release.mediums:
            mediums_data.append(serialize_medium(medium, include))
        data['mediums'] = mediums_data

    return data


def serialize_artist(artist, include):
    data = {
        'id': artist.gid,
        'name': artist.name,
        'sort_name': artist.sort_name,
    }

    if artist.comment:
        data['comment'] = artist.comment

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

    return data

