#!/usr/bin/env python3
"""A module to get the hng stage 0 task cleared"""

from flask import Flask, jsonify
from datetime import datetime

App = Flask(__name__)

#A home route for testing
@App.route('/')
def home():
    return "Hello world"

# The route tp return a json object containing name, date and github repo
@App.route('/Hng_task_0', strict_slashes=False)
def stage_0():
    cur_date = datetime.now().isoformat()
    return jsonify({
        "email": "tolukayode2017@gmail.com",
        "current_datetime": cur_date,
        "github_url": "https://github.com/Toluwaloju0/Hng_Stage_0"
    })

if __name__ == '__main__':
    App.run(host='0.0.0.0', port=4000)