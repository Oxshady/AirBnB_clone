#!/usr/bin/env python3
from json import dump as json_dump, load as json_load
from os.path import exists as file_Exit
class FileStorage:
    """Filestorage"""
    __file_path = "file.json"
    __objects = dict()
    def __init__(self) -> None:
        pass
    def all(self):
        return self.__objects
    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()
    def save(self):
        with open(self.__file_path,"w") as wf:
            json_dump(self.__objects, wf)
    def reload(self):
        if file_Exit(self.__file_path):
            with open(self.__file_path, 'r') as rf:
                self.__objects = json_load(rf)
        else:
            return