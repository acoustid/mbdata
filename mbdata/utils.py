# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from sqlalchemy.orm import class_mapper, defer


def defer_everything_but(entity, *cols):
    m = class_mapper(entity)
    return [defer(k) for k in
            set(p.key for p in m.iterate_properties
                if hasattr(p, 'columns')).difference(cols)]


def get_something_by_gid(query, redirect_model, gid):
    artist = query.filter_by(gid=gid).first()
    if artist is None:
        subquery = query.session.query(redirect_model.new_id_id).\
            filter_by(gid=gid)
        artist = query.filter(redirect_model.new_id.property.primaryjoin.left.in_(subquery)).first()
    return artist

