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


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    """prints html with list of all cities by states"""
    state_dict = storage.all(State)
    return render_template('8-cities_by_states.html', states=state_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
