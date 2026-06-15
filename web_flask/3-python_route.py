#!/usr/bin/python3
"""Start a small Flask web application.

The application listens on 0.0.0.0 port 5000. It adds a /python route
that echoes a text variable and falls back to a default value.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return the greeting shown at the root of the site."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the text shown on the /hbnb page."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return 'C ' plus the text, with underscores shown as spaces."""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Return 'Python ' plus the text (default 'is cool')."""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
