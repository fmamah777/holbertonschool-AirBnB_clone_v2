#!/usr/bin/python3
"""script starts Flask web application and defines route '/'"""

from flask import Flask, render_template
# create Flask application instance, passing it the name of the current module
app = Flask(__name__)


# decorator turns a python function into a Flask view function
@app.route('/', strict_slashes=False)
def hello():
    """ responds to requests to the url showing 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """determines for /hbnb url, 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """defining curl to display text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """define /python/<text> URL behavior"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """define where n must be integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """/ will return an HTML page if n is an int"""
    # render template will look in templates folder for html file designated
    return render_template('5-number.html', n=n)


# start the flask application listening on host address and ports specificied
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
