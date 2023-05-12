#!/usr/bin/python3
"""Defines unittests for base_model.py"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testung the Instantitation of the
    BaseModel class."""

    def test_no_arg(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_id(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

if __name__ == '__main__':
    unittest.main()
