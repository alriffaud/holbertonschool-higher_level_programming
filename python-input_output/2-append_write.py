#!/usr/bin/python3
"""
This module defines the append_write function.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file (UTF8) and
    returns the number of characters added.
    Parameters:
    - filename(str): This is the name of the file to write in.
    - text(str): This is the text to write to the file.
    Returns: The number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return (len(text))
