#!/usr/bin/python3
"""BaseModel
-  defines all common attributes/methods for other classes:
Public instance attributes:
id: string
created_at: datetime - assign with the
current datetime when an instance is created
updated_at: datetime - assign with the
current datetime when an instance
is created and it will be updated
every time you change your object
__str__: should print:
[<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public
instance attributeupdated_at with the current datetime
to_dict(self): returns a dictionary
containing all keys/values of __dict__ of the instance:
"""
import uuid
from json import dumps
from datetime import datetime as dt


class BaseModel:
    """
    BaseModel that all other classes will inherit from
    """

    def __init__(self) -> None:
        """
        constructor for BaseModel
        """
        self.id = (uuid.uuid4()).hex
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self) -> str:
        """
        string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = dt.now()

    def to_dict(self):
        """
        convert object to dictionary to
        be able to converted to json format then load it to json file
        """
        new_dict = dict()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["id"] = self.id
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


if __name__ == "__main__":
    c1 = BaseModel()
    c2 = BaseModel()
    c3 = BaseModel()
    c4 = BaseModel()
    c5 = BaseModel()
    c6 = BaseModel()
    c7 = BaseModel()
    c8 = BaseModel()
    print(c1.id)
    print(c2.id)
    print(c3.id)