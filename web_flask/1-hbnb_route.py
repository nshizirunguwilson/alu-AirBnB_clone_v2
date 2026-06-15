#!/usr/bin/python3
"""Start a small Flask web application.

The application listens on 0.0.0.0 port 5000 and serves two routes:
the root greeting and a short /hbnb page.
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
