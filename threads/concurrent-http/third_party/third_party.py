"""Third party service"""
import time

from flask import Flask

app = Flask(__name__)


@app.route('/slow')
def slow():
    sleep_sec = 3
    time.sleep(sleep_sec)
    return f'Hello World! Slept {sleep_sec}s'

@app.route('/fast')
def fast():
    return f'Hello World! Immediate return'
