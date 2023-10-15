#!/usr/bin/python3
"""
Module for unittesting amenity.py
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    amenity = Amenity()

    def tests_if_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.amenity)),
                         "<class 'models.amenity.Amenity'>")

    def tests_Attributes(self):
        """checks if attributes exist"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_user_inheritance(self):
        """checks if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_types(self):
        """tests if the type of the attribute matches"""
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
