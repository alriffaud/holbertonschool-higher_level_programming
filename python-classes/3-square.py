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
        Parameters:
          - size: This is the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This method defines the area of a square.
        """
        return (self.__size ** 2)
