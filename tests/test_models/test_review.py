#!/usr/bin/python3
"""
Module for unittesting review.py
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Tests instances and methods from Review class"""

    review = Review()

    def test_if_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.review)),
                         "<class 'models.review.Review'>")

    def tests_Attributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(self.review, 'id'), True)
        self.assertEqual(hasattr(self.review, 'user_id'), True)
        self.assertEqual(hasattr(self.review, 'created_at'), True)
        self.assertEqual(hasattr(self.review, 'updated_at'), True)
        self.assertEqual(hasattr(self.review, 'place_id'), True)
        self.assertEqual(hasattr(self.review, 'text'), True)

    def test_types(self):
        """tests if the type of the attribute matches"""
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
