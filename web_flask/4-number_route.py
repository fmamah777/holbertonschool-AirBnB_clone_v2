#!/usr/bin/python3
"""script starts Flask web application and defines route '/'"""

from flask import Flask
# create Flask application instance, passing it the name of the current module
app = Flask(__name__)


# decorator turns a python function into a Flask view function
@app.route('/', strict_slashes=False)
def hello():
    """funct responds ton URL diplaying 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """defining for hbnb url, and display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """url behavior to display text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """define /python/text URL """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """define behavior of /number/<n> URL where n is a integer"""
    return '{} is a number'.format(n)

# start the flask application listening on host address and ports
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

