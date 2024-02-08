#!/usr/bin/python3
"""
In this module, the class Rectangle is defined.
Classes:
- Rectangle: This defines the Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits since BaseGeometry and defines a rectangle.
    Attributes:
    - __width: This is the width of the rectangle.
    - __height: This is the height of the rectangle.
    """
    def __init__(self, width, height):
        """
        This is the initialization method.
        Parameters:
          - width: This is the width of the rectangle.
          - height: This is the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This method returns the area of the rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        This method prints and returns a rectangle description.
        Returns:
        - A string with the rectangle.
        """
        return ("[" + Rectangle.__name__ + "] " + str(self.__width)
                + "/" + str(self.__height))
