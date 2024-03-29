#!/usr/bin/python3
"""
In this module, an empty class is defined.
Classes:
- Rectangle: This class defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.
    Class Attributes:
    - number_of_instances: It represents the number of rectangles.
    Attributes:
    - __width: This is the width of the rectangle.
    - __height: This is the height of the rectangle.
    - __area: This is the area of the rectangle.
    - __perimeter: This is the perimeter of the rectangle.
    Methods:
    - width(self):  This method returns the width of the rectangle.
    - width(self, value): This method sets the value of width.
    - height(self): This method returns the height of the rectangle.
    - height(self, value): This method sets the value of height.
    - area(self): This method returns the area of the rectangle.
    - perimeter(self): This method returns the perimeter of the rectangle.
    - __str__: Is responsible for returning a string representation of the
    object.
    - __repr__: This method returns a string representation of the rectangle
    to be able to recreate a new instance by using eval().
    - __del__: This method print a string when an instance of Rectangle is
    deleted.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        This is the initialization method.
        Parameters:
          - width: This is the width of the rectangle.
          - height: This is the height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        This method returns the width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        This method sets the value of width.
        Parameters:
          - value: It's the new width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This method returns the height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        This method sets the value of height.
        Parameters:
          - value: It's the new height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This method returns the area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        This method returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        This method prints a square with the character #.
        Returns:
        - A string with the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """
        This method return a string representation of the rectangle to be
        able to recreate a new instance by using eval().
        Returns:
        - A string with the rectangle.
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        This method print a string when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This method returns the biggest rectangle based on the area.
        Parameters:
        - rect_1: It's an instance of Rectangle.
        - rect_2: It's an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        This method returns a new Rectangle instance with width == height ==
        size.
        Parameters:
        - size: It's the size of the rectangle instance.
        """
        return (Rectangle(size, size))
