#!/usr/bin/python3
"""
This module defines the 'is_kind_of_class' function.
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is an instance of, or if the
    object is an instance of a class that inherited, the specified class;
    otherwise False.
    Parameters:
    - obj: Represents the object.
    - a_class: Represents the class.
    """
    return (isinstance(obj, a_class))
