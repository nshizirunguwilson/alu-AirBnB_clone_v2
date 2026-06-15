#!/usr/bin/python3
"""Start a small Flask web application.

The application listens on 0.0.0.0 port 5000 and answers the root URL
with a short greeting.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return the greeting shown at the root of the site."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
