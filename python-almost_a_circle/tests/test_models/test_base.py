#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


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

    def test_to_json_string_empty_list(self):
        """
            This function tests the to_json_string method using an empty
            list.
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none_list(self):
        """
            This function tests the to_json_string method with none list.
        """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        """
            This function tests the to_json_string method using a non empty
            list.
        """
        input_list = [{'id': 1, 'name': 'object'}, {'id': 2, 'name': 'item'}]
        result = Base.to_json_string(input_list)
        expected_result = '[{"id": 1, "name": "object"}, '
        expected_result += '{"id": 2, "name": "item"}]'
        self.assertEqual(result, expected_result)

    def setUp(self):
        """
        Create instances for testing.
        """
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.s1 = Square(10, 7, 2, 8)
        self.s2 = Square(2)

    def tearDown(self):
        """
        Clean up created files after each test.
        """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file(self):
        """
        Test if the method saves the correct JSON string to the file.
        """
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = (
                '[{"y": 8, "x": 2, "id": ' + str(self.r1.id) +
                ', "width": 10, "height": 7}, {"y": 0, "x": 0, "id": ' +
                str(self.r2.id) + ', "width": 2, "height": 4}]'
            )
            self.assertEqual(json.loads(content), json.loads(expected_content))

    def test_save_to_file_empty_list(self):
        """
        Test if the method saves an empty list when given an empty list.
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_none_list(self):
        """
        Test if the method saves an empty list when given None.
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_square(self):
        """
        Test if the method saves the correct JSON string to the file.
        """
        Square.save_to_file([self.s1, self.s2])
        with open("Square.json", "r") as file:
            content = file.read()
            expected_content = (
                '[{"y": 2, "x": 7, "id": ' + str(self.s1.id) +
                ', "size": 10}, {"y": 0, "x": 0, "id": ' +
                str(self.s2.id) + ', "size": 2}]'
            )
            self.assertEqual(json.loads(content), json.loads(expected_content))

    def test_save_to_file_empty_list_square(self):
        """
        Test if the method saves an empty list when given an empty list.
        """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_none_list_square(self):
        """
        Test if the method saves an empty list when given None.
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')


if __name__ == '__main__':
    unittest.main()
