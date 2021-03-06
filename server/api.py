# Provides the API endpoints
# REST requests and responses
from functools import wraps
from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, current_app
import jwt
import asyncio
import re
import os
import configparser

from models import db, User, TorrData
from scraper import start_scraping
from rss_feeder import feedParser

api = Blueprint('api', __name__)
loop = asyncio.get_event_loop()

BASEDIR = os.path.abspath(os.path.dirname(__file__))
configParser = configparser.RawConfigParser()
configParser.read(BASEDIR+'\\instance\\external_links.cfg')

# Some of the API points require user authentication: scrape, torr
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

async def preparing_scrap(tag):
    start_scraping(tag)
    return "FALSE"


""" ------------------- API ROUTES ------------------- """
# register user - delete not necessery for this app
@api.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        username = request.get_json()['username']
        password = request.get_json()['password']
        newUser = User(username=username, password=password)
        db.session.add(newUser)
        db.session.commit()
        return jsonify(newUser.to_dict()), 201

@api.route('/rss/<name>', methods=['GET'])
def rss(name):
    if name == 'reddit':
        url = configParser.get('RSS_LINKS', 'REDDIT_RSS')
        feed_parser = feedParser(url)
        return jsonify({'status': 'success', 'rss_entries': feed_parser})
    else:
        return 404

# Podcasts route / using pythons rssfeeder library to process rss feed
@api.route('/podcasts/<name>', methods=['GET'])
def podcasts(name):
    if name == 'recode':
        feed_parser = feedParser('https://feeds.megaphone.fm/recodedecode')
        return jsonify({'status': 'success', 'rss_entries': feed_parser})
    elif name == 'earth911':
        feed_parser = feedParser('https://www.spreaker.com/show/2898651/episodes/feed')
        return jsonify({'status': 'success', 'rss_entries': feed_parser})
    else:
        return 404

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

# start scraping process
@api.route('/scraper', methods=['GET'])
# @token_required
def scraper():#current_user):
    loop.run_until_complete(preparing_scrap('browse/'))
    return "OK"

# search string from the response on torr
@api.route('/scraper/search=', methods=['POST'])
# @token_required
def search():
    if request.method == 'POST':
        result = request.get_json()
        loop.run_until_complete(preparing_scrap('search/' + result['body']))
    return "OK"

# Load data from the database and display them
@api.route('/torr', methods=['GET', 'POST'])
# @token_required
def all_torr_data():
    results = TorrData.query.all()
    torr_data = []

    for entry in results:
        case = {'id': entry.id,'title': re.sub(r'[^a-zA-Z 0-9]', '', entry.title), 'mlink': entry.mlink.strip("\'"), 'image': entry.image, 'date': entry.date, 'size': entry.size}
        torr_data.append(case)

    return jsonify({
        'status': 'success',
        'torr_data': torr_data
        })