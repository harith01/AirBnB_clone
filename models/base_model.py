#!/usr/bin/pyhton3
"""Defines BaseModel Class"""
import datetime
import uuid
import models


class BaseModel:
    """Defines BaseModel Class"""
    def __init__(self, *args, **kwargs):
        if args and len(args) != 0:
            for arg in args:
                continue
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
                else:
                    continue
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates Instance and save"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing all key/value pairs
        of __dict__ of an instance"""
        the_dict = self.__dict__.copy()
        the_dict['__class__'] = self.__class__.__name__
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()
        return the_dict
