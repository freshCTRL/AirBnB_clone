#!/usr/bin/python3
from .. import BaseModel
"""
    This module contains function to store our data informations
"""


class FileStorage:
    """
        This class contains functions needed to communicate our file storage
    """
    __file_path = "file"
    __objects = {}

    def __init__(self):
        """
            Initialises the class
        """
        pass

    def all(self):
        """
        Initialises the (all) method of the instance/class
        :return:  FileStorage.__objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Initialises the (new) method of the instance/class
        """
        if obj:
            FileStorage.__objects = {f"{obj['__class__']}.{obj['id']}": obj}

    def save(self):
        """
        Initialises the (save) method of the instance/class
        """
        import json
        import os
        filename = f"{FileStorage.__file_path}.json"
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                b = json.loads(file.read())
            with open(filename, mode="w", encoding="utf-8") as file:
                b.update(FileStorage.__objects)
                file.write(json.dumps(b))
        else:
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """
        Initialises the (reload) method of the instance/class
        """
        import os
        import json

        filename = f"{FileStorage.__file_path}.json"
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                FileStorage.__objects = BaseModel(**(json.loads(file.read())))

