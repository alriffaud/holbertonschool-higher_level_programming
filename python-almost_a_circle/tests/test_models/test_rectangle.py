#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """
        This function tests the initialization.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 42)

    def test_init_with_negative_values(self):
        """
        This function tests initialization with negative width, height, x,
        and y values.
        """
        with self.assertRaises(ValueError) as exc:
            Rectangle(-5, 10, 1, 2)
        self.assertEqual(str(exc.exception), "width must be > 0")
        with self.assertRaises(ValueError) as exc:
            Rectangle(5, -10, 1, 2)
        self.assertEqual(str(exc.exception), "height must be > 0")
        with self.assertRaises(ValueError) as exc:
            Rectangle(5, 10, -1, 2)
        self.assertEqual(str(exc.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as exc:
            Rectangle(5, 10, 1, -2)
        self.assertEqual(str(exc.exception), "y must be >= 0")

    def test_width_property(self):
        """
        This function tests width property.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        rect.width = 8
        self.assertEqual(rect.width, 8)

    def test_width_property_with_negative_value(self):
        """
        This function tests width property with negative value.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError) as exc:
            rect.width = -8
        self.assertEqual(str(exc.exception), "width must be > 0")

    def test_height_property(self):
        """
        This function tests height property.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.height, 10)
        rect.height = 15
        self.assertEqual(rect.height, 15)

    def test_height_property_with_negative_value(self):
        """
        This function tests height property with negative value.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError) as exc:
            rect.height = -15
        self.assertEqual(str(exc.exception), "height must be > 0")

    def test_x_property(self):
        """
        This function tests x property.
        """
        rect = Rectangle(5, 10, 1)
        self.assertEqual(rect.x, 1)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_x_property_with_negative_value(self):
        """
        This function tests x property with negative value.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError) as exc:
            rect.x = -3
        self.assertEqual(str(exc.exception), "x must be >= 0")

    def test_y_property(self):
        """
        This function tests y property.
        """
        rect = Rectangle(5, 10, 1, 2)
        self.assertEqual(rect.y, 2)
        rect.y = 5
        self.assertEqual(rect.y, 5)

    def test_y_property_with_negative_value(self):
        """
        This function tests y property with negative value.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError) as exc:
            rect.y = -5
        self.assertEqual(str(exc.exception), "y must be >= 0")

    def test_init_with_default_id(self):
        """
        This function tests initialization with default id (None).
        """
        rect = Rectangle(5, 10)
        rect.id = None
        self.assertIsNone(rect.id)

    def test_init_with_custom_id(self):
        """
        This function test initialization with custom id.
        """
        rect = Rectangle(5, 10, id=42)
        self.assertEqual(rect.id, 42)

    def test_init_with_custom_id_after_default_ids(self):
        """
        This function test initialization with custom id after default ids.
        """
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(8, 15, id=42)
        rect3 = Rectangle(3, 7)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 42)
        self.assertEqual(rect3.id, 2)

    def test_init_with_negative_id(self):
        """
        This function tests initialization with negative id.
        """
        rect = Rectangle(8, 15, id=-42)
        self.assertEqual(rect.id, -42)

    def test_area_with_positive_dimensions(self):
        """
        This function tests area with positive width and height.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_area_with_zero_dimensions(self):
        """
        This function tests area with width or height set to zero.
        """
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(0, 10)
            rect.area()
        self.assertEqual(str(exc.exception), "width must be > 0")
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(5, 0)
            rect.area()
        self.assertEqual(str(exc.exception), "height must be > 0")
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(0, 0)
            rect.area()
        self.assertEqual(str(exc.exception), "width must be > 0")

    def test_area_with_negative_dimensions(self):
        """
        This function tests area with negative width or height.
        """
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(-5, 10)
            rect.area()
        self.assertEqual(str(exc.exception), "width must be > 0")
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(5, -10)
            rect.area()
        self.assertEqual(str(exc.exception), "height must be > 0")
        with self.assertRaises(ValueError) as exc:
            rect = Rectangle(-5, -10)
            rect.area()
        self.assertEqual(str(exc.exception), "width must be > 0")

    def test_area_after_width_and_height_change(self):
        """
        This function tests area after changing width and height.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)
        rect.width = 8
        rect.height = 15
        self.assertEqual(rect.area(), 120)

if __name__ == '__main__':
    unittest.main()
