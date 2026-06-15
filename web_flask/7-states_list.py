#!/usr/bin/python3
"""Start a small Flask web application that lists the states.

The application listens on 0.0.0.0 port 5000 and reads the State
objects from the storage engine (FileStorage or DBStorage).
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Close the storage session after every request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Render the list of all states sorted by name (A to Z)."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
