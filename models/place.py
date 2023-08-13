#!/usr/bin/python3
"""
    This module contains the (Place) class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        This is the (Place) class
    """
    city_id = ""  # City.id
    user_id = ""  # User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids: []  # Amenity.id

    def __init__(self):
        """
            Initialises the (Place) class
        """
        super().__init__()

    def to_dict(self):
        """
           returns a dictionary containing all keys/values
           of __dict__ of the instance with __class__ key that have
           class name as value and format the created and updated at keys
        """
        new_dict = {**self.__dict__, "__class__": "Place"}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
