# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from collections import namedtuple
from itsdangerous import URLSafeSerializer, BadSignature
from flask import current_app, abort
from mbdata.api.utils import get_param, response_error
from mbdata.api.errors import INVALID_PARAMETER_ERROR


Page = namedtuple('Page', ['start', 'limit', 'doc', 'score'])


def make_page(start, limit, doc=0, score=0):
    return Page(max(start, 0), limit, doc, score)


def prepare_page_info(results, page):
    signer = URLSafeSerializer(current_app.config['SECRET_KEY'])
    data = {'results_per_page': page.limit, 'total_results': results.numFound}

    if page.start:
        data['start'] = page.start

    if page.start:
        prev_page = make_page(page.start - page.limit, page.limit)
        data['prev_page_token'] = signer.dumps(prev_page)

    if page.start + page.limit < results.numFound:
        last_result = results.results[-1]
        next_page = make_page(page.start + page.limit, page.limit, last_result['[docid]'], last_result['score'])
        data['next_page_token'] = signer.dumps(next_page)

    return data


def parse_page_token(token, limit):
    if not token:
        return make_page(0, limit)

    signer = URLSafeSerializer(current_app.config['SECRET_KEY'])
    try:
        return Page(*signer.loads(token))
    except BadSignature:
        return None


def get_search_params():
    page_token = get_param('page_token', type='text')
    limit = get_param('results', type='int', default=5)

    if limit < 1 or limit > 50:
        raise abort(response_error(INVALID_PARAMETER_ERROR, 'results must be between 1 and 50'))

    page = parse_page_token(page_token, limit)
    if page is None:
        raise abort(response_error(INVALID_PARAMETER_ERROR, 'invalid page token'))

    if limit != page.limit:
        raise abort(response_error(INVALID_PARAMETER_ERROR, 'results does not match the page token'))

    return page


def prepare_search_options(page, fields=None):
    options = {
        'start': page.start,
        'rows': page.limit,
        'fields': '[docid],id,kind',
        'defType': 'edismax',
    }

    if fields:
        options['qf'] = fields

    if page.doc:
        options['pageDoc'] = page.doc

    if page.score:
        options['pageScore'] = page.score

    return options

