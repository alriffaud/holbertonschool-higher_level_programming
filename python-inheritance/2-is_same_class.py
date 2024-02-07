#!/usr/bin/python3
"""
This module defines the 'is_same_class' function.
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly an instance of the
    specified class ; otherwise False.
    Parameters:
    - obj: Represents the object.
    - a_class: Represents the class.
    """
    return (type(obj) is a_class)
