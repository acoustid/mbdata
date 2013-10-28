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
            artist_credit_data['credited_name'] = artist_credit_name.name

        if artist_credit_name.join_phrase:
            artist_credit_data['join_phrase'] = artist_credit_name.join_phrase

        data.append(artist_credit_data)

    return data


def serialize_area(data, name, area, include):
    if not area:
        return

    data[name] = {'name': area.name}

    if include.type and area.type:
        data[name]['type'] = area.type.name

    if include.iso_3166:
        if area.iso_3166_1_codes:
            data[name]['iso_3166_1'] = [r.code for r in area.iso_3166_1_codes]
        if area.iso_3166_2_codes:
            data[name]['iso_3166_2'] = [r.code for r in area.iso_3166_2_codes]
        if area.iso_3166_3_codes:
            data[name]['iso_3166_2'] = [r.code for r in area.iso_3166_3_codes]

    if include.part_of:
        serialize_area(data[name], 'part_of', area.part_of, include)


def serialize_work(work, include):
    data = {
        'id': work.gid,
        'name': work.name,
    }

    if include.iswc:
        data['iswcs'] = [iswc.iswc for iswc in work.iswcs]

    return data


def serialize_recording(recording, include):
    data = {
        'id': recording.gid,
        'name': recording.name,
    }

    if recording.length:
        data['length'] = recording.length / 1000.0

    if include.artist:
        data['artist'] = recording.artist_credit.name
    elif include.artists:
        data['artists'] = serialize_artist_credit(recording.artist_credit)

    if include.isrc:
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

    if include.artist:
        data['artist'] = track.artist_credit.name
    elif include.artists:
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
            tracks_data.append(serialize_track(track, include.tracks))
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
        for type in release_group.secondary_types:
            data['secondary_types'].append(type.secondary_type.name)

    if include.artist:
        data['artist'] = release_group.artist_credit.name
    elif include.artists:
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

    if include.artist:
        data['artist'] = release.artist_credit.name
    elif include.artists:
        data['artists'] = serialize_artist_credit(release.artist_credit)

    if not no_release_group and include.release_group:
        data['release_group'] = serialize_release_group(release.release_group, include.release_group)

    if not no_mediums and include.mediums:
        mediums_data = []
        for medium in release.mediums:
            mediums_data.append(serialize_medium(medium, include.mediums))
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

    if include.areas:
        serialize_area(data, 'area', artist.area, include.areas)
        serialize_area(data, 'begin_area', artist.begin_area, include.areas)
        serialize_area(data, 'end_area', artist.end_area, include.areas)

    if include.ipi:
        data['ipis'] = [ipi.ipi for ipi in artist.ipis]

    if include.isni:
        data['isnis'] = [isni.isni for isni in artist.isnis]

    return data


def serialize_label(label, include):
    data = {
        'id': label.gid,
        'name': label.name,
        'sort_name': label.sort_name,
    }

    if label.comment:
        data['comment'] = label.comment

    serialize_partial_date(data, 'begin_date', label.begin_date)
    serialize_partial_date(data, 'end_date', label.end_date)

    if label.ended:
        data['ended'] = True

    if label.type:
        data['type'] = label.type.name

    if include.areas:
        serialize_area(data, 'area', label.area, include.areas)

    if include.ipi:
        data['ipis'] = [ipi.ipi for ipi in label.ipis]

    if include.isni:
        data['isnis'] = [isni.isni for isni in label.isnis]

    return data

