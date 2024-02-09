#!/usr/bin/python3
"""
This module defines the 'to_json_string' function.
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string).
    Parameters:
    - my_obj: This is the object to represent.
    Returns: A string with the JSON representation.
    """
    return (json.dumps(my_obj))
