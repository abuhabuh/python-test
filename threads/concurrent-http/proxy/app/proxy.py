"""Proxy server for third party.
"""
import requests

from flask import Flask

app = Flask(__name__)


@app.route('/fast-third_party')
def fast():
    # http://third_party is the docker image name specified in the
    # docker-compose.yml file
    res = requests.get('http://third_party:5000/fast')
    return f'3rd Party says: {res.text}\n'

@app.route('/slow-third-party')
def slow():
    # http://third_party is the docker image name specified in the
    # docker-compose.yml file
    res = requests.get('http://third_party:5000/slow')
    return f'3rd Party says: {res.text}\n'
