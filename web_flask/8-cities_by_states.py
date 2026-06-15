#!/usr/bin/python3
"""Start a small Flask web application that lists states and their cities.

The application listens on 0.0.0.0 port 5000 and reads the State and
City objects from the storage engine (FileStorage or DBStorage).
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Close the storage session after every request."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Render every state (A to Z) with its cities listed underneath."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
