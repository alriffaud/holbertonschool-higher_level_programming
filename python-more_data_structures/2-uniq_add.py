#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    This function adds all unique integers in a list (only once for each
    integer).
    """
    if not my_list:
        return (0)
    sum = 0
    for num in set(my_list):
        sum += num
    return (sum)
