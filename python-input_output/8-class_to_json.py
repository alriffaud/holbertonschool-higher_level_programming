#!/usr/bin/python3
"""
This module defines the 'from_json_string' function.
"""


def class_to_json(obj):
    """
    This function returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object.
    Parameters:
    - obj: This is an instance of a Class.
    Returns: The object represented by the string.
    """
    json_dict = {}
    attributes = obj.__dict__
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return (json_dict)
