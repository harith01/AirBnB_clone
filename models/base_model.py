#!/usr/bin/python3
"""Defines the BaseModel Class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines the BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initializes an instance of BaseModel"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
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
