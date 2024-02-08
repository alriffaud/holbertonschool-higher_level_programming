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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
