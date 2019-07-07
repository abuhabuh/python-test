"""Third party service
"""
import time

from flask import Flask

app = Flask(__name__)


@app.route('/slow')
def slow():
    sleep_sec = 3
    time.sleep(sleep_sec)
    return f'third-party:slow -- slept {sleep_sec}s\n'

@app.route('/fast')
def fast():
    return f'third-party:fast\n'
