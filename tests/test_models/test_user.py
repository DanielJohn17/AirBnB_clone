#!/usr/bin/python3
"""Test Module for User"""
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """Test Class for User"""

    my_user = User()

    def test_User_exist(self):
        self.assertEqual(str(type(self.my_user)),
                         "<class 'models.user.User'>")

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.my_user, 'id'))
        self.assertTrue(hasattr(self.my_user, 'created_at'))
        self.assertTrue(hasattr(self.my_user, 'updated_at'))
        self.assertTrue(hasattr(self.my_user, 'email'))
        self.assertTrue(hasattr(self.my_user, 'password'))
        self.assertTrue(hasattr(self.my_user, 'first_name'))
        self.assertTrue(hasattr(self.my_user, 'last_name'))

    def test_types(self):
        """tests if the type of attribute is correct"""
        self.assertIsInstance(self.my_user.id, str)
        self.assertIsInstance(self.my_user.created_at, datetime.datetime)
        self.assertIsInstance(self.my_user.updated_at, datetime.datetime)
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)


if __name__ == "__main__":
    unittest.main()
