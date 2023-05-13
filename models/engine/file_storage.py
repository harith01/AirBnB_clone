#!/usr/bin/python4
"""Defines FileStorage class"""
import json
from models.base_model import BaseModel
from os.path import exists


class FileStorage:
    """Defines FileStorage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return class attribute <__objects>"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new instance to the attribute <__objects>"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes <__objects> to a JSON file"""
        dict_rep = {}
        for key, value in FileStorage.__objects.items():
            dict_rep[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dict_rep, file)

    def reload(self):
        """Deserializes the JSON file to <__objects>"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                dict_rep = json.load(file)
            for key, value in dict_rep.items():
                FileStorage.__objects[key] = BaseModel(**value)
