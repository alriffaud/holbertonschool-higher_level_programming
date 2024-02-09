#!/usr/bin/python3
"""
This module defines the read_file function.
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout.
    Parameters:
    - filename(str): This is the name of the file to read and print.
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
