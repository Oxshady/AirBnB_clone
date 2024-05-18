#!/usr/bin/python3
"""The Place class defines properties for a location including
city, user, name, description, room and
bathroom numbers, guest capacity, price, location
coordinates, and amenities."""

from models.base_model import BaseModel as Cb


class City(Cb):
    """The `City` class represents a city
    with attributes for state ID and name."""

    state_id = ""
    name = ""
