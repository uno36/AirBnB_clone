#!/usr/bin/python3
""" Review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review that inherits from BaseModel
    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
