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
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        self.__area = value ** 2

    def my_print(self):
        """
        This method prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end="")
            print()
