#!/usr/bin/python3
"""
In this module, a Square class is defined.
"""


class Square:
    """
    This class defines a square.
    Attributes:
    - __size: This is the size of the square.
    Methods:
    - area: Defines the area of a square.
    """

    def __init__(self, size=0):
        """
        This is the initialization method.
        Args:
            size (int): This is the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__area = size ** 2

    def area(self):
        """
        This method returns the area of a square.
        """
        return (self.__area)

    @property
    def size(self):
        """
        This method returns the size of a square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the value of size.
        Args:
            value (int): This is the new size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        self.__area = value ** 2
