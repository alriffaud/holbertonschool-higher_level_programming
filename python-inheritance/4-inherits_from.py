#!/usr/bin/python3
"""
This module defines the 'inherits_from' function.
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ; otherwise
    False.
    Parameters:
    - obj: Represents the object.
    - a_class: Represents the class.
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
