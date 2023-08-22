#!/usr/bin/python3
"""
    This module contains the class Basemodel
"""
from datetime import datetime
import uuid
from models.__init__ import storage


class BaseModel:
    """
        BaseModel that defines all common
        attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
            initiates new instance
        """
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.strptime(v, dt_format))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def name(self, value):
        """
            set name attr for an instance
        """
        name = "name"
        setattr(self, name, value)
        getattr(self, name)

    def my_number(self, value):
        """
            set my_number attr for an instance
        """
        my_number = "my_number"
        setattr(self, my_number, value)
        getattr(self, my_number)

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
           returns a dictionary containing all keys/values
           of __dict__ of the instance with __class__ key that have
           class name as value and format the created and updated at keys
        """
        new_dict = {**self.__dict__, "__class__": "BaseModel"}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """
            prints the string representation of an object
        """
        return "[{}] ({}) {}".format(self.to_dict()['__class__'],
                                     self.id, self.__dict__)
