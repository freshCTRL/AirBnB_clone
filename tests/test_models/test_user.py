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
        sample_7 = User()
        sample_7.name = "Bisi"
        sample_7.first_name = "Betty"
        sample_7.last_name = "Bar"
        sample_7.email = "airbnb@mail.com"
        sample_7.password = "root"
        self.assertTrue(sample_7.first_name == "Betty")
        self.assertTrue(sample_7.last_name == "Bar")
        self.assertTrue(sample_7.email == "airbnb@mail.com")
        self.assertTrue(sample_7.password == "root")
        self.assertTrue(sample_7.name == "Bisi")
        self.assertIsNotNone(sample_7.id)
        self.assertIsNotNone(sample_7.created_at)
        self.assertIsNotNone(sample_7.updated_at)
        var_a = sample_7.created_at
        sample_7.save()
        self.assertIsNone(sample_7.save())
        self.assertEqual(sample_7.created_at, var_a)
        self.assertNotEqual(sample_7.created_at, sample_7.updated_at)
        self.assertIsNotNone(str(sample_7))

    def test_to_dict_and_reinstantiation(self):
        """
            test for (to_dict) method
        """
        sample_5 = User()
        self.assertIsInstance(sample_5.to_dict(), dict)
        saved_dict = sample_5.to_dict()
        sample_6 = User(**saved_dict)
        self.assertFalse(sample_6 == sample_5)
        self.assertTrue(sample_6.id == sample_5.id)
        self.assertTrue(sample_6.created_at == sample_5.created_at)
        self.assertTrue(sample_6.updated_at == sample_5.updated_at)
        self.assertTrue(sample_6.__class__ == sample_5.__class__)
        self.assertIsInstance(sample_6.created_at, type(sample_5.created_at))
        self.assertIsInstance(sample_6.updated_at, type(sample_5.updated_at))
        self.assertIsInstance(sample_6.__class__, type(sample_5.__class__))
