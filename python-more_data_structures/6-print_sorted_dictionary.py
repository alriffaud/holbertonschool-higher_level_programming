#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    This function prints a dictionary by ordered keys.
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
