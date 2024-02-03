#!/usr/bin/python3
"""
This module defines the say_my_name function.
Functions:
- say_my_name: This function prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>.
    Parameters:
    - first_name (str): Represents the first name.
    - last_name (str): Represents the last name.
    Returns:
    - None.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
