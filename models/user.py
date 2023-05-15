#!/usr/bin/python3
"""Creates a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
