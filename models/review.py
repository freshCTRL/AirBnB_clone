#!/usr/bin/python3
"""
    This module contains the (Review) class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        This is the (Review) class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """
            Initialising the (Review) class
        """
        super().__init__()

    def to_dict(self):
        """
           returns a dictionary containing all keys/values
           of __dict__ of the instance with __class__ key that have
           class name as value and format the created and updated at keys
        """
        new_dict = {**self.__dict__, "__class__": "Review"}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
