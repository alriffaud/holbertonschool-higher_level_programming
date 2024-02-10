#!/usr/bin/python3
"""
This module defines the 'load_from_json_file' function.
"""
import json


def load_from_json_file(filename):
    """
    This function  creates an Object from a “JSON file”.
    Parameters:
    - filename(str): This is the name of the file.
    """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
