#!/usr/bin/python3
def no_c(my_string):
    """
    This function removes all characters c and C from a string.
    Args:
        my_string: string to remove characters c and C
    """
    new_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_str += i
    return (new_str)
