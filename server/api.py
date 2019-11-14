# Provides the API endpoints
# REST requests and responses

from functools import wraps
from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, current_app
import jwt
import asyncio
import re

#REPLACE
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, mapper

from models import db, User
from scraper import start_scraping

api = Blueprint('api', __name__)
loop = asyncio.get_event_loop()


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token.',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token, Reauthentication requtred.',
            'authenticated': False
        }
        # ensure if contains authorization header with string tat looks like JWT
        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(username=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        # validate if JWT is expired
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # unauthorized HTTP status code
        # ensue it is VALID jwt token
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401
    return _verify

async def preparing_scrap():
    start_scraping()
    return "FALSE"


@api.route('/users')
@token_required
def users():
    response = User.query.all()
    return jsonify(response)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify( {'message': 'Invalid creadentials', 'authenticated': False} ), 401

    token = jwt.encode({
        'sub': user.username,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') })





@api.route('/scraper', methods=['GET'])
def scraper():
    loop.run_until_complete(preparing_scrap())
    return "OK"



# Get all models
@api.route('/torr', methods=['GET'])
def all_torr_data():
    #REPLACE
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)
    Data = Base.classes.torrData

    torr_data = []
    results = db.session.query(Data).all()

    for entry in results:
        # print("-------------", entry.mlink.strip("\'"))
        case = {'id': entry.id,'title': re.sub(r'[^a-zA-Z 0-9]', '', entry.title), 'mlink': entry.mlink.strip("\'"), 'image': entry.image, 'date': entry.date, 'size': entry.size}
        torr_data.append(case)

    return jsonify({
        'status': 'success',
        'torr_data': torr_data
        })