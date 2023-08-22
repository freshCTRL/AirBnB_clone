#!/usr/bin/python3
"""
    This module contains function to store our data informations
"""
import datetime
import os
import json
# import copy


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

        def gt(dt_str):
            """
                reversing an isofomarted date
            """
            dt, _, us = dt_str.partition(".")
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
            us = int(us.rstrip("Z"), 10)
            return dt + datetime.timedelta(microseconds=us)

        final = FileStorage.__objects
        all_keys = final.keys()
        for key in all_keys:
            a = final[key]["__class__"]
            del final[key]["__class__"]
            if a == "BaseModel":
                from models.base_model import BaseModel
                final[key] = BaseModel(final[key])  # i needed to import the base_model class
            else:
                from models.user import User
                final[key] = User(final[key])
            frmtd_date = gt(final[key].to_dict()["created_at"])
            final[key].to_dict()["created_at"] = frmtd_date
            frmtd_date = gt(final[key].to_dict()["updated_at"])
            final[key].to_dict()["updated_at"] = frmtd_date
        return final

    def new(self, obj):
        """
            Initialises the (new) method of the instance/class
        """
        if obj:
            if obj.to_dict()['__class__'] != "BaseModel":
                FileStorage.__objects.update({f"{obj.to_dict()['__class__']}.{obj.to_dict()['id']}": obj.to_dict()})
            else:
                a = {f"{obj.to_dict()['__class__']}.{obj.to_dict()['id']}": obj.to_dict()}
                a.update(FileStorage.__objects)
                FileStorage.__objects = a

    def save(self):
        """
            Initialises the (save) method of the instance/class
        """
        filename = f"{FileStorage.__file_path}"
        if os.path.isfile(filename):
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(FileStorage.__objects))
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
