#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    This function prints all integers of a list, in reverse order.
    Args:
        my_list: list of integers
    """
    for i in my_list[::-1]:
        print("{:d}".format(i))
