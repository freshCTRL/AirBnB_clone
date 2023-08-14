#!/usr/bin/python3
"""
    This module contains the (City) class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        The City class
    """
    state_id = ""  # State.id
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Initialises the City class
        """
        super().__init__(self, *args, **kwargs)

    def to_dict(self):
        """
           returns a dictionary containing all keys/values
           of __dict__ of the instance with __class__ key that have
           class name as value and format the created and updated at keys
        """
        new_dict = {**self.__dict__, "__class__": "City"}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
