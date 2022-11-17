#!/usr/bin/python3
"""flask app setup"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(stuff):
    """tears down the session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """prints html with list of all states"""
    state_dict = storage.all(State)
    return render_template('7-states_list.html', states=state_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
