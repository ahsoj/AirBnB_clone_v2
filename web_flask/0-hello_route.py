#!/usr/bin/python3
"""Create Flask Base app"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index page of web page"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
