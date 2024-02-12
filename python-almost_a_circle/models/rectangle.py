#!/usr/bin/python3
"""
In this module, the Rectangle class is defined.
Classes:
- Rectangle: This class defines a rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class defines a rectangle.
    Attributes:
    - __width: This is the width of the rectangle.
    - __height: This is the height of the rectangle.
    Methods:
    - width(self):  This method returns the width of the rectangle.
    - width(self, value): This method sets the value of width.
    - height(self): This method returns the height of the rectangle.
    - height(self, value): This method sets the value of height.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the initialization method.
        Parameters:
          - width: This is the width of the rectangle.
          - height: This is the height of the rectangle.
          - x: This is the x coordinate.
          - y: This is the y coordinate.
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
        self.__x = x
        self.__y = y
        super().__init__(id)

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
