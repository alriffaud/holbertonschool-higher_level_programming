#!/usr/bin/python3
"""
This module defines the print_square function.
Functions:
- print_square: This function prints a square with the character #.
"""


def print_square(size):
    """
    This function prints a square with the character #.
    Parameters:
    - size (int): Represents the size length of the square.
    Returns:
    - None.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
