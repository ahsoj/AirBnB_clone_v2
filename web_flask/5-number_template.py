#!/usr/bin/python3
"""Create Flask Base app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index page of web page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """path /hbnb page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cFun(text):
    """route with argument"""
    rep_text = text.replace('_', ' ')
    return "C {}".format(rep_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonFun(text="is cool"):
    """route with argument"""
    rep_text = text.replace('_', ' ')
    return "Python {}".format(rep_text)


@app.route("/number/<int:n>", strict_slashes=False)
def nFun(n):
    """route with argument"""
    return "{} is number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page if n is int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
