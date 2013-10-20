# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<path:path>')
def main(path=None):
    filename = 'index.html'
    if path and path.startswith('/static/'):
        filename = path[8:]
    return app.send_static_file(filename)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    from werkzeug.wsgi import DispatcherMiddleware
    from mbdata.api.app import app as api_app

    combined_app = DispatcherMiddleware(app, {'/api': api_app})
    run_simple('127.0.0.1', 5000, combined_app, use_reloader=True, use_debugger=True)

