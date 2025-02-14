#!/usr/bin/python3
"""
    Create Flask Base app
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index page of web page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """path /hbnb page"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def cFun(text):
    """route with argument"""
    rep_text = text.replace('_', ' ')
    return "C {}".format(rep_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def pythonFun(text="is cool"):
    """route with argument"""
    rep_text = text.replace('_', ' ')
    return "Python {}".format(rep_text)


@app.route("/number/<int:n>", strict_slashes=False)
def ifNumber(n):
    """route with argument"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
