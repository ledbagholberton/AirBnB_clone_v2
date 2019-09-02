#!/usr/bin/python3
""" start a Flask Web application
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cissome(text):
    return("C {}".format(text.replace("_", " ")))

app.run(host='0.0.0.0', port= 5000)
