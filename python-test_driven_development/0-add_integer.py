#!/usr/bin/python3
"""This module defines the add_integer function."""


def add_integer(a, b=98):
    """
    This function adds 2 integers.
    Parameters:
    - a: Is an integer or float number.
    - b: Is an integer or float number.
    Returns:
    - The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
