#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
import datetime


class TestFileStorage(unittest.TestCase):
    """
        test for class (file_storage)
    """
    def test_all_reload(self):
        """
            test for class (file_storage)
        """
        all_objs = storage.all()
        self.assertFalse(all_objs == {})
        sample = BaseModel()
        saved_id = sample.id
        save_my_created_at = sample.created_at
        sample.save()
        k = storage.all()

        def gt(dt_str):
            """
                reversing an isofomarted date
            """
            dt, _, us = dt_str.partition(".")
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
            us = int(us.rstrip("Z"), 10)
            return dt + datetime.timedelta(microseconds=us)

        for key0 in k.keys():
            if k[key0].to_dict()["id"] == saved_id:
                self.assertEqual(gt(k[key0].to_dict()["created_at"]), save_my_created_at)

        content = storage.reload()
        self.assertFalse(content == {})
        sample.save()
        a = storage.reload()
        self.assertEqual(content, a)

    def test_save_new(self):
        """
            test for class (file_storage)
        """
        # self.assertTrue(storage.__file_path == "main.py")
