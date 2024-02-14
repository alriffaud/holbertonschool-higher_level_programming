#!/usr/bin/python3
"""
Unittest for Square class.
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    This class tests the Square class
    """

    def test_constructor(self):
        """
        This function tests the initialization.
        """
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_init_with_negative_values(self):
        """
        This function tests initialization with negative size value.
        """
        with self.assertRaises(ValueError) as exc:
            Square(-5)
        self.assertEqual(str(exc.exception), "width must be > 0")

    def test_init_with_zero_value(self):
        """
        This function tests initialization with zero size value.
        """
        with self.assertRaises(ValueError) as exc:
            Square(0)
        self.assertEqual(str(exc.exception), "width must be > 0")

    def test_init_with_empty_value(self):
        """
        This function tests initialization with empty value.
        """
        with self.assertRaises(TypeError):
            Square()

    def test_init_with_none_value(self):
        """
        This function tests initialization with None value.
        """
        with self.assertRaises(TypeError) as exc:
            Square(None)
        self.assertEqual(str(exc.exception), "width must be an integer")

    def test_size_property(self):
        """
        This function tests the size property.
        """
        square = Square(3)
        self.assertEqual(square.size, 3)

    def test_size_setter(self):
        """
        This function tests the size setter.
        """
        square = Square(3)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_str_representation(self):
        """
        This function tests the __str__ representation.
        """
        square = Square(4, 2, 3, 10)
        self.assertEqual(str(square), "[Square] (10) 2/3 - 4")

    def test_update_method_args(self):
        """
        This function tests the update method args.
        """
        square = Square(2, 1, 1, 1)
        square.update(7, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (7) 4/5 - 3")

    def test_update_method_kwargs(self):
        """
        This function tests the update method kwargs.
        """
        square = Square(2, 1, 1, 1)
        square.update(id=7, size=3, x=4, y=5)
        self.assertEqual(str(square), "[Square] (7) 4/5 - 3")

    def test_update_method_mixed_args_kwargs(self):
        """
        This function tests the update method args and kwargs.
        """
        square = Square(2, 1, 1, 1)
        square.update(7, size=3, x=4, y=5)
        self.assertEqual(str(square), "[Square] (7) 4/5 - 3")

    def test_to_dictionary_method(self):
        """
        This function tests the dictionary method.
        """
        square = Square(4, 2, 3, 10)
        expected_dict = {'id': 10, 'size': 4, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_to_dictionary_method_after_update(self):
        """
        This function tests the dictionary method after update.
        """
        square = Square(5, 1, 2, 7)
        square.update(8, 3, 4, 5)
        expected_dict = {'id': 8, 'size': 3, 'x': 4, 'y': 5}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
