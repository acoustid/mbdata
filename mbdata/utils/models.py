from mbdata import models
from sqlalchemy import inspect
from sqlalchemy.orm.session import object_session


def get_link_model(entity0, entity1):
    names = sorted([entity0.__name__, entity1.__name__])
    assert all(hasattr(models, name) for name in names)
    return getattr(models, 'Link{0}{1}'.format(*names))


def query_links(obj, target_model):
    session = object_session(obj)
    model = get_link_model(inspect(obj).mapper.class_, target_model)
    query = session.query(model)

    if isinstance(obj, model.entity0.property.mapper.class_):
        query = query.filter_by(entity0=obj)

    if isinstance(obj, model.entity1.property.mapper.class_):
        query = query.filter_by(entity1=obj)

    return query

