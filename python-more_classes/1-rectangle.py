#!/usr/bin/python3
"""
In this module, an empty class is defined.
Classes:
- Rectangle: This class defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.
    Attributes:
    - width: This is the width of the rectangle.
    - height: This is the height of the rectangle.
    Methods:
    - width(self):  This method returns the width of the rectangle.
    - width(self, value): This method sets the value of width.
    - height(self): This method returns the height of the rectangle.
    - height(self, value): This method sets the value of height.
    """
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
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
