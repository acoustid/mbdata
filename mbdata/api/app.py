# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

from flask import Flask, g, request
from pysolr import Solr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mbdata.api.blueprints.artist import blueprint as artist_blueprint
from mbdata.api.blueprints.label import blueprint as label_blueprint
from mbdata.api.blueprints.place import blueprint as place_blueprint
from mbdata.api.blueprints.recording import blueprint as recording_blueprint
from mbdata.api.blueprints.release import blueprint as release_blueprint
from mbdata.api.blueprints.release_group import blueprint as release_group_blueprint
from mbdata.api.blueprints.work import blueprint as work_blueprint
from mbdata.utils import patch_model_schemas, NO_SCHEMAS


app = Flask(__name__)
app.config.from_object('mbdata.api.commonsettings')
app.config.from_envvar('MBDATA_API_SETTINGS')

app.register_blueprint(artist_blueprint, url_prefix='/v1/artist')
app.register_blueprint(label_blueprint, url_prefix='/v1/label')
app.register_blueprint(place_blueprint, url_prefix='/v1/place')
app.register_blueprint(recording_blueprint, url_prefix='/v1/recording')
app.register_blueprint(release_blueprint, url_prefix='/v1/release')
app.register_blueprint(release_group_blueprint, url_prefix='/v1/release_group')
app.register_blueprint(work_blueprint, url_prefix='/v1/work')

Session = engine = None


def setup_db():
    global engine, Session
    engine = create_engine(app.config['DATABASE_URI'], echo=app.config['DATABASE_ECHO'])
    if engine.url.drivername == 'sqlite':  # XXX replace this with explicit schema mapping configuration
        patch_model_schemas(NO_SCHEMAS)
    Session = sessionmaker(bind=engine)


setup_db()


@app.before_request
def before_request():
    g.db = Session()
    g.solr = Solr(app.config['SOLR_URI'])


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    headers = request.headers.get('Access-Control-Request-Headers')
    if headers is not None:
        response.headers['Access-Control-Allow-Headers'] = headers
    return response


if __name__ == "__main__":
    app.run(debug=True)

