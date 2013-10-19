import re
import xml.sax.saxutils
from cStringIO import StringIO
from flask import request, abort, jsonify, current_app, json
from mbdb.api.errors import (
    SUCCESS,
    INVALID_FORMAT_ERROR,
    MISSING_PARAMETER_ERROR,
)


def to_uuid(s):
    if re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', s):
        return s
    raise ValueError('invalid UUID')


def to_enum(s):
    return s.lower()


PARAM_TYPES = {
    'uuid': to_uuid,
    'enum': to_enum,
    'int': int,
}

def get_param(name, type=None, default=None, required=False):
    value = request.args.get(name, type=PARAM_TYPES.get(type, type), default=default)
    if value is None and request:
        abort(response_error(MISSING_PARAMETER_ERROR, 'missing parameter {0}'.format(name)))
    return value


def singular(plural):
    """
    Take a plural English word and turn it into singular

    Obviously, this doesn't work in general. It know just enough words to
    generate XML tag names for list items. For example, if we have an element
    called 'tracks' in the response, it will be serialized as a list without
    named items in JSON, but we need names for items in XML, so those will be
    called 'track'.
    """
    if plural.endswith('ies'):
        return plural[:-3] + 'y'
    if plural.endswith('s'):
        return plural[:-1]
    raise ValueError('unknown plural form %r' % (plural,))


def dumpxml(output, name, value):
    if isinstance(value, dict):
        output.write('<{0}>'.format(name))
        for sub_name, sub_value in value.iteritems():
            dumpxml(output, sub_name, sub_value)
        output.write('</{0}>'.format(name))
    elif isinstance(value, list):
        output.write('<{0}>'.format(name))
        sub_name = singular(name)
        for sub_value in value:
            dumpxml(output, sub_name, sub_value)
        output.write('</{0}>'.format(name))
    else:
        output.write('<{0}>'.format(name))
        output.write(xml.sax.saxutils.escape(unicode(value)).encode('utf8'))
        output.write('</{0}>'.format(name))


def render_xml(data):
    output = StringIO()
    output.write('<?xml version="1.0" encoding="UTF-8"?>')
    for name, value in data.iteritems():
        dumpxml(output, name, value)
    output.flush()
    return current_app.response_class(output.getvalue(),
                                      mimetype='application/xml')


def render_json(data):
    return current_app.response_class(json.dumps(data, ensure_ascii=False, indent=True),
                                      mimetype='application/json')


def render_response(code, message, data):
    response = {
        'response': {
            'status': {
                'code': code,
                'message': message,
                'version': '1.0',
            },
        }
    }
    response['response'].update(data)

    format = get_param('format', type='enum', default='json')
    if format == 'xml':
        return render_xml(response)
    elif format == 'json':
        return render_json(response)
    else:
        abort(response_error(INVALID_FORMAT_ERROR, 'invalid format {0}'.format(format)))


def response_ok(**data):
    return render_response(SUCCESS, 'success', data)


def response_error(code, message, **data):
    response = render_response(code, message, data)
    response.status_code = 400
    return response


def serialize_partial_date(data, name, date):
    if not date:
        return False
    d = data[name] = {'year': date.year}
    if date.month:
        d['month'] = date.month
        if date.day:
            d['day'] = date.day
    return True

