#!/usr/bin/python3
"""
In this module, the class Square is defined.
Classes:
- Square: This defines the Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class inherits since BaseGeometry and defines a square.
    Attributes:
    - __size: This is the size of the square.
    """
    def __init__(self, size):
        """
        This method returns a new Rectangle instance with width == height ==
        size.
        Parameters:
        - size: It's the size of the rectangle instance.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        This method returns the area of the square.
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        This method prints and returns a square description.
        Returns:
        - A string with the square description.
        """
        return ("[" + Square.__name__ + "] " + str(self.__size)
                + "/" + str(self.__size))
