#!/usr/bin/python3

"""
Unittest for BaseModel class. Downloaded from other
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Tests for BaseModel class
    """

    def Test_base(self):
        """Set up"""
        self.base1 = BaseModel()

    def test_class_type(self):
        """Test for correct class type"""
        b = BaseModel()
        self.assertEqual(b.__class__.__name__, "BaseModel")

if __name__ == '__main__':
    unittest.main()
