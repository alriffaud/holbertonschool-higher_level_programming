#!/usr/bin/python3
def remove_char_at(str, n):
    """
    This function creates a copy of the string, removing the character at
    the position n (not the Python way, the “C array index”).
    """
    new_str = ""
    for i in range(len(str)):
        if i == n:
            continue
        new_str += str[i]
    return (new_str)
