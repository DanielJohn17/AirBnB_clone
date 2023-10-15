#!/usr/bin/python3
"""Test Module for City"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test Class for City"""
    my_city = City()

    def test_attribute(self):
        """test for attributes"""
        self.assertEqual(hasattr(self.my_city, "id"), True)
        self.assertEqual(hasattr(self.my_city, "created_at"), True)
        self.assertEqual(hasattr(self.my_city, "updated_at"), True)
        self.assertEqual(hasattr(self.my_city, "state_id"), True)
        self.assertEqual(hasattr(self.my_city, "name"), True)

    def test_class_exist(self):
        """test if City exists"""
        self.assertEqual(str(type(self.my_city)),
                         "<class 'models.city.City'>")

    def test_types(self):
        """tests if the type of attribute is correct"""
        self.assertIsInstance(self.my_city.id, str)
        self.assertIsInstance(self.my_city.created_at, datetime)
        self.assertIsInstance(self.my_city.updated_at, datetime)
        self.assertIsInstance(self.my_city.state_id, str)
        self.assertIsInstance(self.my_city.name, str)


if __name__ == "__main__":
    unittest.main()
