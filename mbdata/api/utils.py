# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

import re
import logging
import xml.sax.saxutils
from six import StringIO, text_type
from flask import request, abort, current_app, json
from mbdata.api.errors import (
    SUCCESS,
    INVALID_FORMAT_ERROR,
    MISSING_PARAMETER_ERROR,
    ERROR_STATUS_CODES,
    ERROR_DEFAULT_STATUS_CODE,
)
from mbdata.utils.models import ENTITY_TYPES


logger = logging.getLogger(__name__)


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
    'text': text_type,
}


def get_param(name, type=None, default=None, required=False, container=None):
    if type and type.endswith('+'):
        assert default is None
        type = type[:-1]
        value = request.args.getlist(name, type=PARAM_TYPES.get(type, type))
        if not value and required:
            abort(response_error(MISSING_PARAMETER_ERROR, 'missing parameter {0}'.format(name)))
        if container is not None:
            value = container(value)
    else:
        value = request.args.get(name, type=PARAM_TYPES.get(type, type), default=default)
        if value is None and required:
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


def dumpxml(output, name, value, parent_name=None):
    if isinstance(value, dict):
        output.write('<{0}>'.format(name))
        for sub_name, sub_value in value.iteritems():
            dumpxml(output, sub_name, sub_value, parent_name=name)
        output.write('</{0}>'.format(name))
    elif isinstance(value, list):
        output.write('<{0}>'.format(name))
        if parent_name == 'relationships' and name in ENTITY_TYPES:
            sub_name = 'relationship'
        else:
            sub_name = singular(name)
        for sub_value in value:
            dumpxml(output, sub_name, sub_value)
        output.write('</{0}>'.format(name))
    else:
        output.write('<{0}>'.format(name))
        output.write(xml.sax.saxutils.escape(text_type(value)).encode('utf8'))
        output.write('</{0}>'.format(name))


def render_xml(data):
    output = StringIO()
    output.write('<?xml version="1.0" encoding="UTF-8"?>')
    for name, value in data.iteritems():
        dumpxml(output, name, value)
    output.flush()
    return current_app.response_class(output.getvalue(),
        content_type='application/xml; charset=UTF-8')


def render_json(data):
    options = {}
    if current_app.config['DEBUG']:
        options['indent'] = 2
    response = json.dumps(data, ensure_ascii=False, **options)
    return current_app.response_class(response,
        content_type='application/json; charset=UTF-8')


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
    logger.debug('response_error(%r, %r, %r)', code, message, data)
    response = render_response(code, message, data)
    response.status_code = ERROR_STATUS_CODES.get(code, ERROR_DEFAULT_STATUS_CODE)
    return response

