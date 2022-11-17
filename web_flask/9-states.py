#!/usr/bin/python3
"""flask app setup"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(stuff):
    """tears down the session"""
    storage.close()


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    """displays list of states, or list of cities in certain state"""
    states = storage.all().values()
    state_selected = None
    if id is not None:
        for state in states:
            if state.id == id:
                state_selected = state
    return render_template("9-states.html", states=states, id=id,
                           state_selected=state_selected)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
