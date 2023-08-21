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
        def gt(dt_str):
            dt, _, us = dt_str.partition(".")
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
            us = int(us.rstrip("Z"), 10)
            return dt + datetime.timedelta(microseconds=us)

        for key in FileStorage.__objects.keys():
            if type(FileStorage.__objects[key]) == str:
                return FileStorage.__objects
            else:
                frmtd_date = gt(FileStorage.__objects[key].to_dict()["created_at"])
                FileStorage.__objects[key].to_dict()["created_at"] = frmtd_date
                frmtd_date = gt(FileStorage.__objects[key].to_dict()["updated_at"])
                FileStorage.__objects[key].to_dict()["updated_at"] = frmtd_date
                kpClsNme = FileStorage.__objects[key].to_dict()["__class__"]
                del FileStorage.__objects[key].to_dict()["__class__"]
                FileStorage.__objects[key] = \
                    "[{}] ({}) {}".format(kpClsNme,
                                          FileStorage.__objects[key].to_dict()["id"],
                                          FileStorage.__objects[key].to_dict())
        return FileStorage.__objects

    def new(self, obj):
        """
            Initialises the (new) method of the instance/class
        """
        if obj:
            try:
                b = {f"{obj.to_dict()['__class__']}.{obj.to_dict()['id']}": obj}
                for key in reversed(b.keys()):
                        first_key = key
                    for k, v in b[first_key].items():
                        if k == "__class__":
                            a = v
                    if a == "BaseModel":
                        FileStorage.__objects.update(b)
                    else:
                        FileStorage.__objects = b.update(FileStorage.__objects)
            except:
                pass

    def save(self):
        """
            Initialises the (save) method of the instance/class
        """
        filename = f"{FileStorage.__file_path}"
        try:
            for key in FileStorage.__objects.keys():
                FileStorage.__objects[key] = FileStorage.__objects[key].to_dict()
            if os.path.isfile(filename):
                with open(filename, mode="w", encoding="utf-8") as file:
                    file.write(json.dumps(FileStorage.__objects))
        except:
            pass

    def reload(self):
        """
            Initialises the (reload) method of the instance/class
        """
        filename = f"{FileStorage.__file_path}"
        try:
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
        except:
            pass
