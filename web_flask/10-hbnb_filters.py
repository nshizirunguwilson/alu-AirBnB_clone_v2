#!/usr/bin/python3
"""Start a small Flask web application that shows the HBNB filters page.

The application listens on 0.0.0.0 port 5000 and reads the State, City
and Amenity objects from the storage engine (FileStorage or DBStorage).
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Close the storage session after every request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Render the filters page with states, cities and amenities."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
