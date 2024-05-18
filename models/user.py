"""The `User` class inherits attributes from
`BaseModel` and defines email, password, first name, and
last name attributes for a user."""

from models.base_model import BaseModel as s_S


class User(s_S):
    """The class `User` defines attributes for email,
    password, first name, and last name for a user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
