#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        This class test the max_integer function.
    """
    def test_max_integer_integers_list(self):
        """
            This function tests the case if the parameter is a list of
            integers.
        """
        list = [1, 2, 3, 4]
        max = max_integer(list=list)
        self.assertEqual(max, 4)
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer_floats_list(self):
        """
            This function tests the case if the parameter is a list of
            floats.
        """
        list = [1.5, 5.4, 13.7, 4.8]
        max = max_integer(list=list)
        self.assertEqual(max, 13.7)

    def test_max_integer_string_list(self):
        """
            This function tests the case if the parameter is a string.
        """
        list = "Hello"
        max = max_integer(list=list)
        self.assertEqual(max, 'o')

    def test_max_integer_value_error_list(self):
        """
            This function tests when one element is a string.
        """
        list = [1, "hello", 3, 4]
        with self.assertRaises(TypeError) as exc:
            max_integer(list=list)
        self.assertEqual(str(exc.exception), "'>' not supported between \
instances of 'str' and 'int'")

    def test_max_integer_None(self):
        """
            This function tests the case if the parameter is None.
        """
        list = None
        with self.assertRaises(TypeError) as exc:
            max_integer(list=list)
        self.assertEqual(str(exc.exception), "object of type 'NoneType' has \
no len()")

    def test_max_integer_empty(self):
        """
            This function tests the case if the list is empty.
        """
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer(()))

    def test_max_integer_not_a_list(self):
        """
            This function tests when the input is not a list.
        """
        list = 123
        with self.assertRaises(TypeError) as exc:
            max_integer(list=list)
        self.assertEqual(str(exc.exception), "object of type 'int' has \
no len()")


if __name__ == '__main__':
    unittest.main()
