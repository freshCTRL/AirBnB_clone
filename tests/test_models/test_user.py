#!/usr/bin/python3
"""
    This module contains tests for the file named user.py
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
        test for class (base_models)
    """
    def test_initialisation_str_save(self):
        """
            test for (init), (str), (save) method
        """
        sample1 = User()
        self.assertIsNotNone(sample1.first_name)
        self.assertIsNotNone(sample1.last_name)
        self.assertIsNotNone(sample1.email)
        self.assertIsNotNone(sample1.password)
        self.assertIsNotNone(sample1.id)
        self.assertIsNotNone(sample1.created_at)
        self.assertIsNotNone(sample1.updated_at)

    def test_to_dict_and_reinstantiation(self):
        """
            test for (to_dict) method
        """
        pass
