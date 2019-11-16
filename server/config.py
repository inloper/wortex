# Settings for the Flask application object

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///d:\\dev\\wortex\\server\\torr.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'thisisthemostsecretkeyever'