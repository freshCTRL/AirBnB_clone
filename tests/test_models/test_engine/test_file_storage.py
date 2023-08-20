#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """
        test for class (file_storage)
    """
    def setUp(self):
        """
            initialising a test...
        """
        pass

    def tearDown(self):
        """
            closing a test...
        """
        pass

    def test_all_reload(self):
        """
            test for class (file_storage)
        """
        all_objs = storage.all()
        self.assertFalse(all_objs == {})
        sample = BaseModel()
        save_my_id = sample.id
        save_my_created_at = sample.created_at
        sample.save()
        k = storage.all()
        saved_key0 = 0
        for key0 in storage.all().keys():
            for key1 in k[key0].keys():
                if key1 == "id":
                    if k[key0][key1] == save_my_id:
                        saved_key0 = key0
                        break
        for key2 in storage.all().keys():
            if key2 == saved_key0:
                self.assertEqual(k[key2]["id"], save_my_id)
        content = storage.reload()
        self.assertFalse(content == {})
        sample.save()
        a = storage.reload()
        self.assertEqual(content, a)
        os.remove("file.json")

    def test_save_new(self):
        """
            test for class (file_storage)
        """
        # self.assertTrue(storage.__file_path == "file.json")
