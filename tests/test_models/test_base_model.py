#!/usr/bin/python3
"""
    This module contains tests for the file named base_model.py
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """
        test for class (base_models)
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

    def test_initialisation_str_save(self):
        """
            test for (init), (str), (save) method
        """
        sample_1 = BaseModel()
        sample_1.name = "Bisi"
        self.assertTrue(sample_1.name == "Bisi")
        self.assertIsNotNone(sample_1.id)
        self.assertIsNotNone(sample_1.created_at)
        self.assertIsNotNone(sample_1.updated_at)
        sample_1.save()
        sample_4 = BaseModel()
        sample_4.name = "My_First_Model"
        sample_4.my_number = 89
        sample_4.save()
        caller = FileStorage()
        val = caller.all()
        for key0 in val.keys():
            if val[key0].to_dict()["id"] == sample_4.id:
                self.assertEqual(val[key0].to_dict()["my_number"], 89)
                break
        a = caller.reload()
        self.assertNotEqual(a, val)
        self.assertIsNotNone(str(sample_4))

    def test_to_dict_and_reinstantiation(self):
        """
            test for (to_dict) method
        """
        sample_2 = BaseModel()
        self.assertIsInstance(sample_2.to_dict(), dict)
        saved_dict = sample_2.to_dict()
        sample_3 = BaseModel(**saved_dict)
        self.assertFalse(sample_3 == sample_2)
        self.assertTrue(sample_3.id == sample_2.id)
        self.assertTrue(sample_3.created_at == sample_2.created_at)
        self.assertTrue(sample_3.updated_at == sample_2.updated_at)
        self.assertTrue(sample_3.__class__ == sample_2.__class__)
        self.assertIsInstance(sample_3.created_at, type(sample_2.created_at))
        self.assertIsInstance(sample_3.updated_at, type(sample_2.updated_at))
        self.assertIsInstance(sample_3.__class__, type(sample_2.__class__))
