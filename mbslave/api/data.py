from sqlalchemy import sql
from sqlalchemy.orm import joinedload, subqueryload
from sqlalchemy.inspection import inspect
from mbdata.utils.models import get_entity_type_model, get_link_model, ENTITY_TYPES
from mbdata.models import (
    Area,
    Artist,
    Label,
    Link,
    LinkAreaArea,
    LinkType,
    Place,
    Release,
    Recording,
    ReleaseGroup,
    Work,
)


def load_areas(session, objs, include):
    attrs = []
    ids = set()
    for obj in objs:
        mapper = inspect(obj).mapper
        for relationship in mapper.relationships:
            if not issubclass(relationship.mapper.class_, Area):
                continue
            attr = relationship.key
            for column in relationship.local_columns:
                id = getattr(obj, mapper.get_property_by_column(column).key)
                if id is not None:
                    attrs.append((obj, id, attr))
                    ids.add(id)

    areas = fetch_areas(session, ids, include)
    for obj, id, attr in attrs:
        setattr(obj, attr, areas[id])


def fetch_areas(session, ids, include):
    areas = {}
    if not ids:
        return areas

    options = []

    if include.iso_3166:
        options.append(joinedload('iso_3166_1_codes'))
        options.append(joinedload('iso_3166_2_codes'))
        options.append(joinedload('iso_3166_3_codes'))

    if include.type:
        options.append(joinedload('type'))

    query = session.query(Area).filter(Area.id.in_(ids)).options(*options)
    for area in query:
        areas[area.id] = area

    if include.part_of and areas:
        _fetch_parent_areas(session, areas, options)

    return areas


def _fetch_parent_areas(session, areas, options):
    for area in areas.values():
        area.part_of = None

    link_type_id_query = session.query(LinkType.id).\
        filter_by(gid='de7cc874-8b1b-3a05-8272-f3834c968fb7').\
        as_scalar()

    area_parent_query = session.query(
            LinkAreaArea.entity1_id.label('child_id'),
            LinkAreaArea.entity0_id.label('parent_id'),
        ).\
        select_from(LinkAreaArea).\
        join(Link, LinkAreaArea.link_id == Link.id).\
        filter(Link.link_type_id == link_type_id_query).\
        subquery()

    if session.bind.dialect.name == 'postgresql':
        _fetch_parent_areas_cte(session, area_parent_query, areas, options)
    else:
        _fetch_parent_areas_iterate(session, area_parent_query, areas, options)


def _fetch_parent_areas_iterate(session, area_parent_query, areas, options):
    while True:
        area_ids = [area.id for area in areas.values() if area.part_of is None]

        query = session.query(Area, area_parent_query.c.child_id).\
            filter(Area.id == area_parent_query.c.parent_id).\
            filter(area_parent_query.c.child_id.in_(area_ids)).\
            options(*options)

        found = False
        for area, child_id in query:
            area.part_of = None
            areas[area.id] = area
            areas[child_id].part_of = area
            found = True

        if not found:
            break


def _fetch_parent_areas_cte(session, area_parent_query, areas, options):
    area_ids = [area.id for area in areas.values() if area.part_of is None]

    area_ancestors_cte = session.query(
            area_parent_query.c.child_id,
            area_parent_query.c.parent_id,
            sql.literal(1).label('depth')
        ).\
        select_from(area_parent_query).\
        filter(area_parent_query.c.child_id.in_(area_ids)).\
        cte(name='area_ancestors', recursive=True)

    area_ancestors_cte = area_ancestors_cte.union_all(
        session.query(
            area_parent_query.c.child_id,
            area_parent_query.c.parent_id,
            area_ancestors_cte.c.depth + 1
        ).
        select_from(area_ancestors_cte).
        join(area_parent_query, area_ancestors_cte.c.parent_id == area_parent_query.c.child_id)
    )

    query = session.query(Area, area_ancestors_cte.c.child_id, area_ancestors_cte.c.depth).\
        filter(Area.id == area_ancestors_cte.c.parent_id).\
        order_by(area_ancestors_cte.c.depth).options(*options)

    for area, child_id, depth in query:
        area.part_of = None
        areas[area.id] = area
        areas[child_id].part_of = area


def query_artist(db, include):
    return prepare_artist_query(db.query(Artist), include)


def query_label(db, include):
    return prepare_label_query(db.query(Label), include)


def query_place(db, include):
    return prepare_place_query(db.query(Place), include)


def query_recording(db, include):
    return prepare_recording_query(db.query(Recording), include)


def query_release(db, include):
    return prepare_release_query(db.query(Release), include)


def query_release_group(db, include):
    return prepare_release_group_query(db.query(ReleaseGroup), include)


def query_work(db, include):
    return prepare_work_query(db.query(Work), include)


def prepare_artist_query(query, include, prefix=""):
    query = query.\
        options(joinedload(prefix + "gender")).\
        options(joinedload(prefix + "type"))

    if include.ipi:
        query = query.options(subqueryload(prefix + "ipis"))

    if include.isni:
        query = query.options(subqueryload(prefix + "isnis"))

    return query


def prepare_label_query(query, include, prefix=""):
    query = query.options(joinedload(prefix + "type"))

    if include.ipi:
        query = query.options(subqueryload(prefix + "ipis"))

    if include.isni:
        query = query.options(subqueryload(prefix + "isnis"))

    return query


def prepare_place_query(query, include, prefix=""):
    return query.options(joinedload(prefix + "type"))


def prepare_recording_query(query, include, prefix=""):
    return prepare_artist_credits_subquery(query, include, prefix)


def prepare_release_query(query, include, prefix=""):
    query = query.\
        options(joinedload(prefix + "status")).\
        options(joinedload(prefix + "packaging")).\
        options(joinedload(prefix + "language")).\
        options(joinedload(prefix + "script"))

    query = prepare_artist_credits_subquery(query, include, prefix)

    if include.release_group:
        query = prepare_release_group_query(query, include.release_group, prefix + "release_group.")

    if include.mediums:
        query = query.options(subqueryload(prefix + "mediums"))
        query = prepare_medium_query(query, include.mediums, prefix + "mediums.")

    return query


def prepare_medium_query(query, include, prefix=""):
    query = query.options(joinedload(prefix + "format"))

    if include.tracks:
        query = query.options(subqueryload(prefix + "tracks"))
        query = prepare_track_query(query, include.tracks, prefix + "tracks.")

    return query


def prepare_track_query(query, include, prefix=""):
    query = prepare_artist_credits_subquery(query, include, prefix)

    if include.recording:
        query = query.options(subqueryload(prefix + "recording"))
        query = prepare_recording_query(query, include, prefix + "recording.")

    return query


def prepare_release_group_query(query, include, prefix=""):
    query = query.\
        options(joinedload(prefix + "type")).\
        options(subqueryload(prefix + "secondary_types")).\
        options(joinedload(prefix + "secondary_types.secondary_type", innerjoin=True))

    query = prepare_artist_credits_subquery(query, include, prefix)

    return query


def prepare_artist_credits_subquery(query, include, prefix):
    if include.artist or include.artists:
        query = query.options(joinedload(prefix + "artist_credit", innerjoin=True))
    if include.artists:
        query = query.\
            options(subqueryload(prefix + "artist_credit.artists")).\
            options(joinedload(prefix + "artist_credit.artists.artist", innerjoin=True))

    return query


def prepare_url_query(query, include, prefix=""):
    return query


def prepare_work_query(query, include, prefix=""):
    return query.options(joinedload(prefix + "type"))


def load_links(db, all_objs, include):
    for type in ENTITY_TYPES:
        type_include = include.check(type)
        if type_include:
            load_links_by_target_type(db, all_objs, type, type_include)


ENTITY_TYPE_PREPARE_FUNCS = {
    'artist': prepare_artist_query,
    'label': prepare_label_query,
    'place': prepare_place_query,
    'recording': prepare_recording_query,
    'release': prepare_release_query,
    'release_group': prepare_release_group_query,
    'url': prepare_url_query,
    'work': prepare_work_query,
}


def load_links_by_target_type(db, all_objs, target_type, include):
    attr = '{0}_links'.format(target_type)

    grouped_objs = {}
    for obj in all_objs:
        setattr(obj, attr, [])
        model = inspect(obj).mapper.class_
        grouped_objs.setdefault(model, {})[obj.id] = obj

    for model, objs in grouped_objs.items():
        _load_links_by_types(db, objs, attr, model, target_type, include)


def _load_links_by_types(db, objs, attr, source_model, target_type, include):
    target_model = get_entity_type_model(target_type)
    model = get_link_model(source_model, target_model)
    query = db.query(model).\
        options(joinedload("link", innerjoin=True)).\
        options(joinedload("link.link_type", innerjoin=True))

    if model.entity0.property.mapper.class_ == model.entity1.property.mapper.class_:
        _load_links_by_types_one_side(model, query, objs, attr, include, "entity0", "entity1", target_type)
        _load_links_by_types_one_side(model, query, objs, attr, include, "entity1", "entity0", target_type)
    else:
        if source_model == model.entity0.property.mapper.class_:
            _load_links_by_types_one_side(model, query, objs, attr, include, "entity0", "entity1", target_type)
        else:
            _load_links_by_types_one_side(model, query, objs, attr, include, "entity1", "entity0", target_type)


def _load_links_by_types_one_side(model, query, objs, attr, include, source_attr, target_attr, target_type):
    source_id_attr = source_attr + "_id"
    query = query.filter(getattr(model, source_id_attr).in_(objs))

    query = query.options(joinedload(target_attr, innerjoin=True))
    query = ENTITY_TYPE_PREPARE_FUNCS[target_type](query, include, target_attr + ".")

    for link in query:
        obj = objs.get(getattr(link, source_id_attr))
        if obj is not None:
            getattr(obj, attr).append(link)

