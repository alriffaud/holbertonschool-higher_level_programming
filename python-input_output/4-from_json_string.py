#!/usr/bin/python3
"""
This module defines the 'from_json_string' function.
"""
import json


def from_json_string(my_str):
    """
    This function returns an object (Python data structure) represented by a
    JSON string.
    Parameters:
    - my_str(str): This is the string that represents an object.
    Returns: The object represented by the string.
    """
    return (json.loads(my_str))
