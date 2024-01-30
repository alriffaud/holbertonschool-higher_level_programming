#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    This function prints a dictionary by ordered keys.
    """
    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2
    return (new_dictionary)
