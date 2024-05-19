#!/usr/bin/python3
"""
The `FileStorage` class provides methods
for storing and managing objects in a JSON file."""

from json import dump as json_dump, load as json_load
from os.path import exists as file_Exit


class FileStorage:
    """Filestorage class that maintain storage system"""

    __file_path = "file.json"
    __objects = dict()

    def __init__(self) -> None:
        """
        The above function is a Python constructor that does nothing.
        """
        pass

    def all(self):
        """
        The `all` function returns all objects stored in the class instance.
        :return: The `all` method is returning
        the `__objects` attribute of the class instance.
        """
        return self.__objects

    def new(self, obj):
        """
        The function `new` adds a new object to a dictionary
        with the object's class name and id as the
        key.

        :param obj: The `obj` parameter in the `new` method
        is an object that you are passing to the
        method. It seems like the method is adding this object
        to a dictionary called `__objects` with a
        key that combines the class name of the object and
        its id, and the value being the object
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        The `save` function writes the contents
        of `self.__objects` to a file specified by
        `self.__file_path` in JSON format.
        """
        new = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json_dump(new, f)

    def reload(self):
        """
        The `reload` function reads and loads JSON data
        from a file specified by `self.__file_path` if
        the file exists.
        :return: In the provided code snippet, if the condition
        `file_Exit(self.__file_path)` is true,
        the objects stored in the file specified by `self.__file_path`
        are loaded into `self.__objects`
        using `json_load(rf)`. If the condition is false, the function
        returns without performing any
        further actions.
        """
        from models.base_model import BaseModel as b
        from models.user import User as u
        from models.amenity import Amenity as a
        from models.city import City as c
        from models.state import State as s
        from models.review import Review as r
        from models.place import Place as p

        self.__classe = {
            "BaseModel": b,
            "User": u,
            "Amenity": a,
            "City": c,
            "State": s,
            "Review": r,
            "Place": p,
        }

        if file_Exit(self.__file_path):
            with open(self.__file_path, "r") as f:
                obj_dict = json_load(f)
                for key, value in obj_dict.items():
                    cl = value["__class__"]
                    if cl in self.__classe:
                        self.__objects[key] = self.__classe[cl](**value)
        else:
            return
