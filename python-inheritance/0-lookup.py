#!/usr/bin/python3
"""
This module defines the 'lookup' function.
"""


def lookup(obj):
    """
    This function returns the list of available attributes and methods of
    an object.
    Parameters:
    - obj: Represents the object.
    """
    return (list(dir(obj)))
