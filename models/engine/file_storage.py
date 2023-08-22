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

        def gt(dt_str):
            """
                reversing an isofomarted date
            """
            dt, _, us = dt_str.partition(".")
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
            us = int(us.rstrip("Z"), 10)
            return dt + datetime.timedelta(microseconds=us)

        final2 = copy.deepcopy(FileStorage.__objects)
        all_keys2 = final2.keys()
        final = {}
        for key in all_keys2:
            if type(final2[key]) == dict:
                if final2[key]['__class__'] == "BaseModel":
                    from models.base_model import BaseModel
                    final.update({key: BaseModel(**final2[key])})
                else:  # if final2[key]['__class__'] == "User"  to be updated 
                    from models.user import User  # when new child classes are added
                    final.update({key: User(**final2[key])})
            else:
                final.update({key: final2[key]})

        all_keys = final.keys()
        for key in all_keys:
            del final[key].to_dict()["__class__"]
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
                FileStorage.__objects.update({f"{obj.to_dict()['__class__']}.{obj.to_dict()['id']}": obj})
            else:
                a = {f"{obj.to_dict()['__class__']}.{obj.to_dict()['id']}": obj}
                a.update(FileStorage.__objects)
                FileStorage.__objects = a

    def save(self):
        """
            Initialises the (save) method of the instance/class
        """
        filename = f"{FileStorage.__file_path}"
        keep_me2 = copy.deepcopy(FileStorage.__objects)
        keep_me = {}
        for key in keep_me2.keys():
            if type(keep_me2[key]) != dict:
                keep_me.update({key: keep_me2[key].to_dict()})
            else:
                keep_me.update({key: keep_me2[key]})

        if os.path.isfile(filename):
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(keep_me))
        else:
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(keep_me))

    def reload(self):
        """
            Initialises the (reload) method of the instance/class
        """
        filename = f"{FileStorage.__file_path}"
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                FileStorage.__objects = json.loads(file.read())
