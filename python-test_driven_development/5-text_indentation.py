#!/usr/bin/python3
"""
This module defines the text_indentation function.
Functions:
- text_indentation: This function prints a text with 2 new lines after each of
these characters: ., ? and :.
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these
    characters: ., ? and :.
    Parameters:
    - size (int): Represents the size length of the square.
    Returns:
    - None.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Remove leading and trailing whitespaces from the entire text
    text = text.strip()
    characters = {'.', '?', ':'}
    modified_text = ""
    i = 0
    while i < len(text):
        modified_text += text[i]
        if text[i] in characters:
            modified_text += "\n\n"
            while i + 1 != len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
    print(modified_text, end="")
