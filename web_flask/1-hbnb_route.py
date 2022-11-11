#!/usr/bin/python3
'''flask application setup'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''prints hello HBHB'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world_hbnb():
    '''prints HBHB'''
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
