#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import unittest.mock


class TestRectangleClass(unittest.TestCase):
    """
    This class tests the Rectangle class
    """
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

    def test_init_with_empty_value(self):
        """
        This function tests initialization with empty value.
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_init_with_none_value(self):
        """
        This function tests initialization with None value.
        """
        with self.assertRaises(TypeError):
            Rectangle(None)

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

    def test_init_with_no_int_value(self):
        """
        This function tests initialization with no int value.
        """
        with self.assertRaises(TypeError) as exc:
            Rectangle(2.5, 3)
        self.assertEqual(str(exc.exception), "width must be an integer")

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

    def test_display(self):
        """
        This function tests display method.
        """
        rect = Rectangle(3, 2, 1, 2)
        expected_output = "\n\n ###\n ###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        """
        This function tests __str__ method.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_display_with_nonzero_dimensions(self):
        """
        This function tests display with non-zero width and height.
        """
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_position(self):
        """
        This function tests display with x and y positions.
        """
        rect = Rectangle(3, 2, 1, 2)
        expected_output = "\n\n ###\n ###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation_with_default_id(self):
        """
        This function tests __str__ method with default id (None).
        """
        rect = Rectangle(5, 10)
        expected_str = "[Rectangle] (1) 0/0 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_str_representation_with_custom_id(self):
        """
        This function tests __str__ method with custom id.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_update_with_args_only(self):
        """
        This function tests update with positional arguments only.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        rect.update(23, 8, 16, 4, 5)
        self.assertEqual(rect.id, 23)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 16)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_update_with_kwargs_only(self):
        """
        This function tests update with keyword arguments only.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        rect.update(id=23, width=8, height=16, x=4, y=5)
        self.assertEqual(rect.id, 23)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 16)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_update_with_args_and_kwargs(self):
        """
        This function tests update with both positional and keyword arguments.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        rect.update(23, width=8, height=16, x=4, y=5)
        self.assertEqual(rect.id, 23)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 16)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_update_without_args_and_kwargs(self):
        """
        This function tests update with both positional and keyword arguments.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        rect.update()
        self.assertEqual(rect.id, 42)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_update_with_invalid_args(self):
        """
        This function tests update with invalid positional arguments.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        with self.assertRaises(ValueError) as exc:
            rect.update(23, -8, 16, 4, 5)
        self.assertEqual(str(exc.exception), "width must be > 0")
        with self.assertRaises(ValueError) as exc:
            rect.update(23, 8, -16, 4, 5)
        self.assertEqual(str(exc.exception), "height must be > 0")

    def test_update_with_invalid_kwargs(self):
        """
        This function tests update with invalid keyword arguments.
        """
        rect = Rectangle(5, 10, 1, 2, 42)
        with self.assertRaises(ValueError) as exc:
            rect.update(id=23, width=-8, height=16, x=4, y=5)
        self.assertEqual(str(exc.exception), "width must be > 0")
        with self.assertRaises(ValueError) as exc:
            rect.update(id=23, width=8, height=-16, x=4, y=5)
        self.assertEqual(str(exc.exception), "height must be > 0")


if __name__ == '__main__':
    unittest.main()
