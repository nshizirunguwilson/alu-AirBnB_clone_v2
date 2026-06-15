# web_flask

This folder holds the Flask web application for the AirBnB clone. Each
numbered script starts a small web server and adds one more route than the
previous one, so you can follow the project step by step.

## Requirements

```bash
pip3 install Flask
```

Every script listens on `0.0.0.0` port `5000`. Run one with:

```bash
python3 -m web_flask.0-hello_route
```

The storage backed scripts (7 to 10) read their data through `models.storage`,
so they work with both `FileStorage` and `DBStorage`. To use the database
engine, set the usual environment variables, for example:

```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
```

## Scripts and routes

| Script | Routes | What it shows |
| --- | --- | --- |
| `0-hello_route.py` | `/` | "Hello HBNB!" |
| `1-hbnb_route.py` | `/`, `/hbnb` | adds "HBNB" |
| `2-c_route.py` | `/c/<text>` | "C " + text (underscores become spaces) |
| `3-python_route.py` | `/python/(<text>)` | "Python " + text, default "is cool" |
| `4-number_route.py` | `/number/<n>` | "n is a number" only when n is an integer |
| `5-number_template.py` | `/number_template/<n>` | HTML page with the number |
| `6-number_odd_or_even.py` | `/number_odd_or_even/<n>` | HTML page saying even or odd |
| `7-states_list.py` | `/states_list` | every state sorted by name |
| `8-cities_by_states.py` | `/cities_by_states` | states with their cities |
| `9-states.py` | `/states`, `/states/<id>` | all states, or one state with its cities |
| `10-hbnb_filters.py` | `/hbnb_filters` | the filters page (states, cities, amenities) |

## Templates and static files

* `templates/` holds the Jinja templates rendered by the scripts above.
* `static/styles/` holds the CSS copied from `web_static` (the `.popover`
  rule was given a 300px max height with a scroll bar).
* `static/images/` holds the logo and icon used by the filters page.

## Notes

* All routes use `strict_slashes=False`.
* The storage backed scripts close the SQLAlchemy session after every
  request with an `@app.teardown_appcontext` handler.
