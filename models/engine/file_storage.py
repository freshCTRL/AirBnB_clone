#!/usr/bin/python3
"""
    This module contains function to store our data informations
"""
import datetime
import os
import json


class FileStorage:
    """
        This class contains functions needed to communicate our file storage
    """
    __file_path = "file.json"
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
        filename = f"{FileStorage.__file_path}"
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                b = json.loads(file.read())
            with open(filename, mode="w", encoding="utf-8") as file:
                for key in reversed(FileStorage.__objects.keys()):
                    first_key = key
                for k, v in FileStorage.__objects[first_key].items():
                    if k == "__class__":
                        a = v
                if a == "BaseModel":
                    FileStorage.__objects.update(b)
                    file.write(json.dumps(FileStorage.__objects))
                else:
                    b.update(FileStorage.__objects)
                    file.write(json.dumps(b))
        else:
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """
        Initialises the (reload) method of the instance/class
        """
        filename = f"{FileStorage.__file_path}"
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                FileStorage.__objects = json.loads(file.read())

            all_keys = FileStorage.__objects.keys()
            for key in all_keys:
                def gt(dt_str):
                    dt, _, us = dt_str.partition(".")
                    dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
                    us = int(us.rstrip("Z"), 10)
                    return dt + datetime.timedelta(microseconds=us)
                frmtd_date = gt(FileStorage.__objects[key]["created_at"])
                FileStorage.__objects[key]["created_at"] = frmtd_date
                frmtd_date = gt(FileStorage.__objects[key]["updated_at"])
                FileStorage.__objects[key]["updated_at"] = frmtd_date
                kpClsNme = FileStorage.__objects[key]["__class__"]
                del FileStorage.__objects[key]["__class__"]
                FileStorage.__objects[key] =\
                    "[{}] ({}) {}".format(kpClsNme,
                                          FileStorage.__objects[key]["id"],
                                          FileStorage.__objects[key])
