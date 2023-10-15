#!/usr/bin/python3
"""Module for FileStorage Test"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test Class for FileStorage class"""
    model = BaseModel()

    def test_class_instance(self):
        """check instance"""
        self.assertIsInstance(storage, FileStorage)

    def test_hasattr(self):
        """check if attribute exists"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)

    def test_save_storage(self):
        """check if the JSON file exists"""
        self.model.save()

        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_store_BaseModel(self):
        """Test save, update and relod functions"""
        self.model.name = "First"
        self.model.save()
        new_dict = self.model.to_dict()
        all_objs = storage.all()

        key = "{}.{}".format(new_dict["__class__"], new_dict["id"])

        self.assertEqual(new_dict["name"], "First")
        self.assertEqual(key in all_objs, True)

        created_at_1 = new_dict["created_at"]
        updated_at_1 = new_dict["updated_at"]

        self.model.name = "Second"
        self.model.save()
        new_dict = self.model.to_dict()
        all_objs = storage.all()

        self.assertEqual(new_dict["name"], "Second")

        created_at_2 = new_dict["created_at"]
        updated_at_2 = new_dict["updated_at"]

        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)


if __name__ == "__main__":
    unittest.main()
