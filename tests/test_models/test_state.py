#!/usr/bin/python3
"""
    This module contains tests for the file named base_model.py
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
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
        sample_1 = State()
        self.assertIsNotNone(sample_1.name)
        sample_1.name = "Osun"
        self.assertTrue(sample_1.name == "Osun")
        self.assertIsNotNone(sample_1.id)
        self.assertIsNotNone(sample_1.created_at)
        self.assertIsNotNone(sample_1.updated_at)

    def test_to_dict_and_reinstantiation(self):
        """
            test for (to_dict) method
        """
        sample_2 = State()
        self.assertIsInstance(sample_2.to_dict(), dict)
        saved_dict = sample_2.to_dict()
        sample_3 = State(**saved_dict)
        self.assertFalse(sample_3 == sample_2)
        self.assertTrue(sample_3.id == sample_2.id)
        self.assertTrue(sample_3.created_at == sample_2.created_at)
        self.assertTrue(sample_3.updated_at == sample_2.updated_at)
        self.assertTrue(sample_3.__class__ == sample_2.__class__)
        self.assertIsInstance(sample_3.created_at, type(sample_2.created_at))
        self.assertIsInstance(sample_3.updated_at, type(sample_2.updated_at))
        self.assertIsInstance(sample_3.__class__, type(sample_2.__class__))
