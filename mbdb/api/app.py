from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mbdb.api.artist import blueprint as artist_blueprint


app = Flask(__name__)
app.config.from_object('mbdb.api.commonsettings')
app.config.from_envvar('MBDB_API_SETTINGS')

app.register_blueprint(artist_blueprint, url_prefix='/1.0/artist')

engine = create_engine(app.config['DATABASE_URI'], echo=app.config['DATABASE_ECHO'])
Session = sessionmaker(bind=engine)


@app.before_request
def before_request():
    g.db = Session()


@app.teardown_request
def teardown_request(exception):
    g.db.close()


if __name__ == "__main__":
	app.run(debug=True)

