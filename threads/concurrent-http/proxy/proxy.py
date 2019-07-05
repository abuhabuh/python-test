# Proxy server for third party.
import requests

from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    res = requests.get('http://localhost:5000/slow')
    return f'3rd Party says: {res.text}'
