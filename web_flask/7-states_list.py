#!/usr/bin/python3
"""flask app setup"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """prints html with list of all states"""
    state_dict = storage.all()
    return render_template('7-states_list.html', states=states.values())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
