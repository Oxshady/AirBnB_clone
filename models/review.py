"""The Review class inherits attributes from
the BaseModel class and defines attributes for a review
object such as place_id, user_id, and text."""

from models.base_model import BaseModel as Rb


class Review(Rb):
    """The class Review defines attributes for a review object,
    including place_id, user_id, and text."""

    place_id = ""
    user_id = ""
    text = ""
