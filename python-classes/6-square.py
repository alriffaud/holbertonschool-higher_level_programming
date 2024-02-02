#!/usr/bin/python3
"""
In this module, a Square class is defined.
Classes:
- Square: A class to define a square.
"""


class Square:
    """
    This class defines a square.
    Attributes:
    - size: This is the size of the square.
    - area: This is the area of the square.
    - position: This is the position of the square.
    Methods:
    - area: Defines the area of a square.
    - size(self): Returns the size of a square.
    - size(self, value): Sets the value of size.
    - position: Sets the position of the square. 
    - my_print: prints in stdout the square with the character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This is the initialization method.
        Parameters:
          - size: This is the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2 or not all(isinstance(element, int) and
                                element >= 0 for element in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__area = size ** 2
        self.__position = tuple(position)

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
        return (self.__size)

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
            
    @property
    def position(self):
        """
        This method returns the position of a square.
        """
        return (self.__position)
    
    @position.setter
    def position(self, value):
        """
        This method sets the position of the square.
        """
        if len(value) != 2 or not all(isinstance(element, int) and
                                element >= 0 for element in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = tuple(value)

    def my_print(self):
        """
        This method prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for column in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
