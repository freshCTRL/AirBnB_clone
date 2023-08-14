#!/usr/bin/python3
"""
    This module contains the (State) class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        This is the (State) class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Initialising the (State) class
        """
        super().__init__(self, *args, **kwargs)

    def to_dict(self):
        """
           returns a dictionary containing all keys/values
           of __dict__ of the instance with __class__ key that have
           class name as value and format the created and updated at keys
        """
        new_dict = {**self.__dict__, "__class__": "State"}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
