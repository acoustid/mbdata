# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from mbdata.utils.models import ENTITY_TYPES, get_link_target


def serialize_partial_date(data, name, date):
    if not date:
        return

    d = data[name] = {'year': date.year}
    if date.month:
        d['month'] = date.month
        if date.day:
            d['day'] = date.day


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
            data[name]['iso_3166_3'] = [r.code for r in area.iso_3166_3_codes]

    if include.part_of:
        serialize_area(data[name], 'part_of', area.part_of, include)


def serialize_relationships(data, obj, include):
    if include.relationships:
        data['relationships'] = {}

    for type in ENTITY_TYPES:
        if include.relationships.check(type):
            links_data = []
            for link in getattr(obj, '{0}_links'.format(type), ()):
                link_data = {'type': link.link.link_type.name}

                serialize_partial_date(link_data, 'begin_data', link.link.begin_date)
                serialize_partial_date(link_data, 'end_data', link.link.end_date)

                if link.link.ended:
                    link_data['ended'] = True

                link_data[type] = ENTITY_SERIALIZERS[type](get_link_target(link, obj), include.relationships.check(type))
                links_data.append(link_data)

            if links_data:
                data['relationships'][type] = links_data


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


def serialize_url(url, include):
    return {'id': url.gid, 'url': url.url}


def serialize_work(work, include):
    data = {
        'id': work.gid,
        'name': work.name,
    }

    if work.type:
        work['type'] = work.type.name

    if include.iswc:
        data['iswcs'] = [iswc.iswc for iswc in work.iswcs]

    serialize_relationships(data, work, include)

    return data


def serialize_recording(recording, include):
    data = {
        'id': recording.gid,
        'name': recording.name,
    }

    if recording.comment:
        data['comment'] = recording.comment

    if recording.length:
        data['length'] = recording.length / 1000.0

    if recording.video:
        data['video'] = True

    if include.artist:
        data['artist'] = recording.artist_credit.name
    elif include.artists:
        data['artists'] = serialize_artist_credit(recording.artist_credit)

    if include.isrc:
        data['isrcs'] = [isrc.isrc for isrc in recording.isrcs]

    serialize_relationships(data, recording, include)

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

    if release_group.comment:
        data['comment'] = release_group.comment

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

    serialize_relationships(data, release_group, include)

    return data


def serialize_release(release, include):
    data = {
        'id': release.gid,
        'name': release.name,
    }

    if release.comment:
        data['comment'] = release.comment

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

    if include.release_group:
        data['release_group'] = serialize_release_group(release.release_group, include.release_group)

    if include.mediums:
        mediums_data = []
        for medium in release.mediums:
            mediums_data.append(serialize_medium(medium, include.mediums))
        data['mediums'] = mediums_data

    serialize_relationships(data, release, include)

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

    serialize_relationships(data, artist, include)

    return data


def serialize_label(label, include):
    data = {
        'id': label.gid,
        'name': label.name,
    }

    if label.comment:
        data['comment'] = label.comment

    serialize_partial_date(data, 'begin_date', label.begin_date)
    serialize_partial_date(data, 'end_date', label.end_date)

    if label.ended:
        data['ended'] = True

    if label.type:
        data['type'] = label.type.name

    if include.area:
        serialize_area(data, 'area', label.area, include.area)

    if include.ipi:
        data['ipis'] = [ipi.ipi for ipi in label.ipis]

    if include.isni:
        data['isnis'] = [isni.isni for isni in label.isnis]

    serialize_relationships(data, label, include)

    return data


def serialize_place(place, include):
    data = {
        'id': place.gid,
        'name': place.name,
    }

    if place.comment:
        data['comment'] = place.comment

    serialize_partial_date(data, 'begin_date', place.begin_date)
    serialize_partial_date(data, 'end_date', place.end_date)

    if place.address:
        data['address'] = place.address

    if place.ended:
        data['ended'] = True

    if place.type:
        data['type'] = place.type.name

    if place.coordinates:
        data['coordinates'] = {
            'latitude': place.coordinates[0],
            'longitude': place.coordinates[1],
        }

    if include.area:
        serialize_area(data, 'area', place.area, include.area)

    serialize_relationships(data, place, include)

    return data


ENTITY_SERIALIZERS = {
    'artist': serialize_artist,
    'label': serialize_label,
    'place': serialize_place,
    'recording': serialize_recording,
    'release_group': serialize_release_group,
    'release': serialize_release,
    'url': serialize_url,
    'work': serialize_work,
}

