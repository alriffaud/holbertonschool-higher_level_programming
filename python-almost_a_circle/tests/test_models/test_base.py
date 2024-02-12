#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
        This class test the Base class.
    """
    def test_init_with_id(self):
        """
            This function tests the initialization with a specified id.
        """
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
        """
        This function tests the initialization without a specified id.
        """
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_nb_objects_increment(self):
        """
        This function tests that __nb_objects attribute is incremented
        correctly.
        """
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_init_with_custom_id_after_increment(self):
        """
        This function test initialization with a specified id after
        __nb_objects increment.
        """
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base(id=100)
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 100)
        self.assertEqual(obj3.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)


if __name__ == '__main__':
    unittest.main()
