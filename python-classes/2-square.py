#!/usr/bin/python3
"""
In this module, a Square class is defined.
"""


class Square:
    """
    This class defines a square.
    Attributes:
    - __size: This is the size of the square.
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
