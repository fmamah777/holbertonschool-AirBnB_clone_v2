#!/usr/bin/python3
<<<<<<< HEAD
""" Start a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print a hello """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Print C <text> """
    return 'C {}'.format(text).replace('_', ' ')


if __name__ == '__main__':
=======
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


@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    '''prints text'''
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


if __name__ == "__main__":
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096
    app.run(host='0.0.0.0', port=5000)
