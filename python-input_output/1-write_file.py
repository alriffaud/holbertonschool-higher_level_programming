#!/usr/bin/python3
"""
This module defines the write_file function.
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) and returns the number
    of characters written.
    Parameters:
    - filename(str): This is the name of the file to write in.
    - text(str): This is the text to write to the file.
    Returns: The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return (len(text))
