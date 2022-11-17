#!/usr/bin/python3
<<<<<<< HEAD
""" Start a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print a hello """
    return 'Hello HBNB!'


if __name__ == '__main__':
=======
'''flask application setup'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''prints hello HBHB'''
    return "Hello HBNB!"

if __name__ == "__main__":
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096
    app.run(host='0.0.0.0', port=5000)
