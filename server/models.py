'''
Data classes for the application
'''
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# DB MODELS User for authentication and login
class User(db.Model):
    __tablename__ = 'users'

    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(120), unique=True, nullable=False)
    password    = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password, method='sha256')

    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if not username or not password:
            return None

        user = cls.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id, username=self.username)

# DB MODEL  for scraped data
class TorrData(db.Model):
    __tablename__ = 'torrData'

    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.Text)
    mlink   = db.Column(db.Text)
    image   = db.Column(db.Text)
    date    = db.Column(db.Text)
    size    = db.Column(db.Text)

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    mlink=self.mlink,
                    image=self.mliimagenk,
                    date=self.date,
                    size=self.size)