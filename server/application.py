# Creates a Flask app instance and registers the database object

from flask import Flask
from flask_cors import CORS

def create_app(app_name='WORTEX'):
    app = Flask(app_name, instance_relative_config=True)
    # app.config.from_object('config.BaseConfig') # moving from .py file to instance/flask.cfg
    app.config.from_pyfile('flask.cfg')

    cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

    from api import api
    app.register_blueprint(api, url_prefix='/api')

    from models import db
    db.init_app(app)

    return app