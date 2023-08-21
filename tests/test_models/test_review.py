#!/usr/bin/python3
"""
    This module contains tests for the file named file_storage.py
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
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
        sample_1 = Review()
        self.assertIsNotNone(sample_1.user_id)
        self.assertIsNotNone(sample_1.text)
        self.assertIsNotNone(sample_1.place_id)
        sample_1.name = "Bisi"
        self.assertIsInstance(sample_1.user_id, str)
        self.assertIsInstance(sample_1.text, str)
        self.assertTrue(sample_1.name == "Bisi")
        self.assertIsNotNone(sample_1.id)
        self.assertIsNotNone(sample_1.created_at)
        self.assertIsNotNone(sample_1.updated_at)

    def test_to_dict_and_reinstantiation(self):
        """
            test for (to_dict) method
        """
        sample_2 = Review()
        self.assertIsInstance(sample_2.to_dict(), dict)
        saved_dict = sample_2.to_dict()
        sample_3 = Review(**saved_dict)
        self.assertFalse(sample_3 == sample_2)
        self.assertTrue(sample_3.id == sample_2.id)
        self.assertTrue(sample_3.created_at == sample_2.created_at)
        self.assertTrue(sample_3.updated_at == sample_2.updated_at)
        self.assertTrue(sample_3.__class__ == sample_2.__class__)
        self.assertIsInstance(sample_3.created_at, type(sample_2.created_at))
        self.assertIsInstance(sample_3.updated_at, type(sample_2.updated_at))
        self.assertIsInstance(sample_3.__class__, type(sample_2.__class__))
