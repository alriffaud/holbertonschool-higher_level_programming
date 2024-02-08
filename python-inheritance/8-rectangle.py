#!/usr/bin/python3
"""
In this module, the class BaseGeometry is defined.
Classes:
- BaseGeometry: This defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    This is the class that defines a BaseGeometry.
    Methods:
    - area(self): raises an Exception with the message area() is not
    implemented.
    - integer_validator: This method validates the variable value.
    """
    def area(self):
        """
        This method raises an Exception with the message area() is not
        implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates the variable value.
        Parameters:
        - name(str): It's the of the BaseGeometry.
        - value(int): It's  the value of the BaseGeometry
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
