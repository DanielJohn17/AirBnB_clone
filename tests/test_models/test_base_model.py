#!/usr/bin/python3
"""Module for BaseModel Test."""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Suite of Console Tests """

    my_model = BaseModel()

    def test_BaseModel(self):
        """Test attributes value of a BaseModel instance"""
        self.my_model.name = "Daniel"
        self.my_model.my_num = 20
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json["name"])
        self.assertEqual(self.my_model.my_num, my_model_json["my_num"])
        self.assertEqual("BaseModel", my_model_json["__class__"])

    def test_save(self):
        """Checks if save method works"""
        self.my_model.name = "first"
        self.my_model.save()
        first_dic = self.my_model.to_dict()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

        self.my_model.name = "second"
        self.my_model.save()
        second_dic = self.my_model.to_dict()

        self.assertEqual(first_dic["created_at"], second_dic["created_at"])
        self.assertNotEqual(first_dic["updated_at"], second_dic["updated_at"])


if __name__ == "__main__":
    unittest.main()
