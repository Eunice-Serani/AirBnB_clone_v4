#!/usr/bin/python3
<<<<<<< HEAD
""" Starts a Flash Web Application """
=======
""" This starts a Flash Web Application """
>>>>>>> 55258619358786d12e0620469871bcf4dff75b28
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
<<<<<<< HEAD
=======
from uuid import uuid4
>>>>>>> 55258619358786d12e0620469871bcf4dff75b28
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

<<<<<<< HEAD

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
=======
@app.teardown_appcontext
def close_db(error):
    """ This removes the current SQLAlchemy Session """
    storage.close()

@app.route('/0-hbnb/', strict_slashes=False)
>>>>>>> 55258619358786d12e0620469871bcf4dff75b28
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

<<<<<<< HEAD
    return render_template('100-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places)
=======
    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid4())
>>>>>>> 55258619358786d12e0620469871bcf4dff75b28


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
