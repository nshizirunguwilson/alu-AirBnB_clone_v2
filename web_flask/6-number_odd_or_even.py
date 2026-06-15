#!/usr/bin/python3
"""Start a small Flask web application.

The application listens on 0.0.0.0 port 5000. It adds a
/number_odd_or_even/<n> route that renders an HTML page telling whether
n is even or odd.
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return 'n is a number' only when n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render an HTML page that shows the number n."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Render an HTML page that says whether n is even or odd."""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
