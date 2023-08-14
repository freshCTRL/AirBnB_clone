#!/usr/bin/python3
"""
    This module contains the amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        The amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Initialising the class
        """
        super().__init__(self, *args, **kwargs)

    def to_dict(self):
        """
           returns a dictionary containing all keys/values
           of __dict__ of the instance with __class__ key that have
           class name as value and format the created and updated at keys
        """
        new_dict = {**self.__dict__, "__class__": "Amenity"}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
