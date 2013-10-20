from flask import Flask

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def main(path=None):
    return app.send_static_file('index.html')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    from werkzeug.wsgi import DispatcherMiddleware
    from mbdb.api.app import app as api_app

    combined_app = DispatcherMiddleware(app, {'/api': api_app})
    run_simple('127.0.0.1', 5000, combined_app, use_reloader=True)

