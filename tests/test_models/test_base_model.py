#!/usr/bin/python3
"""
Base model unittest
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    BaseModel unittest
    """

    def test_class(self):
        """
        test if the object is a type of BaseModel
        """

        obj = BaseModel()
        self.assertEqual(type(obj), BaseModel)

    def test_attr(self):
        """
        test attributs
        """

        obj = BaseModel()
        obj.astring = "tata"
        obj.alist = ["Hello", 19]
        obj.anint = 24
        obj.atuple = (4, "une tulipe")
        self.assertNotEqual(obj.id, None)
        self.assertNotEqual(obj.created_at, None)
        self.assertNotEqual(obj.updated_at, None)
        self.assertEqual(obj.astring, "tata")
        self.assertEqual(obj.alist, ["Hello", 19])
        self.assertEqual(obj.anint, 24)
        self.assertEqual(obj.atuple, (4, "une tulipe"))
        self.assertEqual(type(obj.atuple), tuple)

    def test_dict(self):
        """
        test dictionary and if the dictionary have correct keys
        """

        obj = BaseModel()
        my_dict = obj.__dict__
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("id", my_dict)

    def test_str(self):
        """
        test the format of str
        """

        obj = BaseModel()
        obj_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(obj_str, str(obj))
if __name__ == "__main__":
    unittest.main()
