#!/usr/bin/python3
"""
In this module, the class BaseGeometry is defined.
"""


class BaseGeometry:
    """
    This is the class that defines a BaseGeometry.
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
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
