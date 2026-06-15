#!/usr/bin/python3
"""Start a small Flask web application that shows states and one state.

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


@app.route('/states', strict_slashes=False)
def states():
    """Render the list of all states sorted by name (A to Z)."""
    state_list = sorted(storage.all(State).values(),
                        key=lambda state: state.name)
    return render_template('9-states.html', mode='list', states=state_list)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Render one state with its cities, or a 'Not found!' message."""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', mode='single', state=state)
    return render_template('9-states.html', mode='not_found')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
