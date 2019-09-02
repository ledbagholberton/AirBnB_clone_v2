#!/usr/bin/python3
""" start a Flask Web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """ Print HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cissome(text):
    """ Print C + <name> without underscore """
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonalone():
    """ Print Python is cool .. by defaul """
    return("Python is cool")


@app.route('/python/<text>')
def pythonissome(text):
    """ Print Python + <name> without underscore """
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<nummer>')
def numberisint(nummer):
    """ Print a number if is number """
    if nummer.isdigit():
        return("{} is a number".format(nummer))

app.run(host='0.0.0.0', port=5000)
