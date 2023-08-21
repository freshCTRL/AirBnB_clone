#!/usr/bin/python3
"""
    This module contains function to store our data informations
"""
import datetime
import os
import json
import copy


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
        final = copy.deepcopy(FileStorage.__objects)

        def gt(dt_str):
            dt, _, us = dt_str.partition(".")
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
            us = int(us.rstrip("Z"), 10)
            return dt + datetime.timedelta(microseconds=us)

        all_keys = final.keys()
        for key in all_keys:
            frmtd_date = gt(final[key]["created_at"])
            final[key]["created_at"] = frmtd_date
            frmtd_date = gt(final[key]["updated_at"])
            final[key]["updated_at"] = frmtd_date
            kpClsNme = final[key]["__class__"]
            del final[key]["__class__"]
            final[key] = \
                "[{}] ({}) {}".format(kpClsNme,
                                      final[key]["id"],
                                      final[key])
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
