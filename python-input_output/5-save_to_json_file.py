#!/usr/bin/python3
"""
This module defines the 'save_to_json_file' function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation.
    Parameters:
    - my_obj: This is the object to represent.
    - filename(str): This is the name of the file to write in.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
