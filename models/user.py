#!/usr/bin/python3
"""
    This module contains the (User) class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        This is the (User) class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """
            Initialising the (User) class
        """
        super().__init__()

    def to_dict(self):
        """
           returns a dictionary containing all keys/values
           of __dict__ of the instance with __class__ key that have
           class name as value and format the created and updated at keys
        """
        new_dict = {**self.__dict__, "__class__": "User"}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
