from sqlalchemy import sql
from sqlalchemy.orm import joinedload
from sqlalchemy.inspection import inspect
from mbdata.models import Area, Link, LinkType, LinkAreaArea


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
    for area in areas.itervalues():
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
        area_ids = [area.id for area in areas.itervalues() if area.part_of is None]

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
    area_ids = [area.id for area in areas.itervalues() if area.part_of is None]

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
        ).\
        select_from(area_ancestors_cte).\
        join(area_parent_query, area_ancestors_cte.c.parent_id == area_parent_query.c.child_id)
    )

    query = session.query(Area, area_ancestors_cte.c.child_id, area_ancestors_cte.c.depth).\
        filter(Area.id == area_ancestors_cte.c.parent_id).\
        order_by(area_ancestors_cte.c.depth).options(*options)

    for area, child_id, depth in query:
        area.part_of = None
        areas[area.id] = area
        areas[child_id].part_of = area

