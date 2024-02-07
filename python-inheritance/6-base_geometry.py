#!/usr/bin/python3
"""
In this module, the class BaseGeometry is defined.
"""


class BaseGeometry:
    """
    This is the class that defines a BaseGeometry.
    Methods:
    - area(self):
    """
    def area(self):
        """
        This method raises an Exception with the message area() is not
        implemented.
        """
        raise Exception("area() is not implemented")
