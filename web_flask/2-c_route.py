#!/usr/bin/python3
"""Create Flask Base app"""

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


@app.route("/c/<text>", strict_slashes=False)
def cFun(text):
    """route with argument"""
    return f"C {text.replace("_", " ")}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
