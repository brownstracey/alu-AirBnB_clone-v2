#!/usr/bin/python3
""" Starts a Flask web application to display States and Cities from the database """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Displays an HTML page with a list of all State objects """
    states = storage.all(State)  # Fetch all State objects
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Displays an HTML page with details about a specific State if found """
    states = storage.all(State)  # Fetch all State objects
    state = None
    for s in states.values():
        if s.id == id:
            state = s
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """ Removes the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
