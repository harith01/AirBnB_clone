#!/usr/bin/python3
"""Defines the BaseModel Class"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines the BaseModel Class"""

    def __init__(self):
        """Initializes an instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the object representation in string format"""
        return "{} ({}) {}".format(self.__class__.__name__, self.id,
                                   self.__dict__)

    def save(self):
        """Update the public instance attributr 'update_at' with
        the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of an instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
