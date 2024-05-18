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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """
        The `save` function writes the contents
        of `self.__objects` to a file specified by
        `self.__file_path` in JSON format.
        """
        with open(self.__file_path, "w") as wf:
            json_dump(self.__objects, wf)

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
        if file_Exit(self.__file_path):
            with open(self.__file_path, "r") as rf:
                self.__objects = json_load(rf)
        else:
            return
