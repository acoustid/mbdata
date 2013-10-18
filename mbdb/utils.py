from sqlalchemy.orm import class_mapper, defer


def defer_everything_but(entity, *cols):
    m = class_mapper(entity)
    return [defer(k) for k in
            set(p.key for p in m.iterate_properties
                if hasattr(p, 'columns')).difference(cols)]

