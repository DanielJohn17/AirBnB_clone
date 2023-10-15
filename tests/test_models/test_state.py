#!/usr/bin/python3
"""Module for State"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Test Class for State"""
    my_state = State()

    def test_attribute(self):
        """test for attributes"""
        self.assertEqual(hasattr(self.my_state, "id"), True)
        self.assertEqual(hasattr(self.my_state, "created_at"), True)
        self.assertEqual(hasattr(self.my_state, "updated_at"), True)
        self.assertEqual(hasattr(self.my_state, "name"), True)

    def test_class_exist(self):
        """test if the class exists"""
        self.assertEqual(str(type(self.my_state)),
                         "<class 'models.state.State'>")

    def test_types(self):
        """tests if the type of attribute is correct"""
        self.assertIsInstance(self.my_state.id, str)
        self.assertIsInstance(self.my_state.created_at, datetime)
        self.assertIsInstance(self.my_state.updated_at, datetime)
        self.assertIsInstance(self.my_state.name, str)


if __name__ == '__main__':
    unittest.main()
