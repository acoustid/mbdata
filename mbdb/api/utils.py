import re
import xml.sax.saxutils
from cStringIO import StringIO
from flask import request, abort, jsonify, current_app


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
        abort(response_error(1, 'missing parameter {0}'.format(name)))
    return value


def dumpxml(output, name, value):
    if isinstance(value, dict):
        output.write('<{0}>'.format(name))
        for sub_name, sub_value in value.iteritems():
            dumpxml(output, sub_name, sub_value)
        output.write('</{0}>'.format(name))
    elif isinstance(value, list):
        output.write('<{0}_list>'.format(name))
        for sub_value in value:
            dumpxml(output, name, sub_value)
        output.write('</{0}_list>'.format(name))
    else:
        output.write('<{0}>'.format(name))
        output.write(xml.sax.saxutils.escape(unicode(value)))
        output.write('</{0}>'.format(name))


def xmlify(data):
    output = StringIO()
    output.write('<?xml version="1.0" encoding="UTF-8"?>')
    for name, value in data.iteritems():
        dumpxml(output, name, value)
    output.flush()
    return current_app.response_class(output.getvalue(),
                                      mimetype='application/xml')


def response_ok(**data):
    return serialize_response(0, 'success', data)


def response_error(code, message, **data):
    response = serialize_response(code, message, data)
    response.status_code = 400
    return response


def serialize_response(code, message, data):
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
        return xmlify(response)
    else:
        return jsonify(response)

