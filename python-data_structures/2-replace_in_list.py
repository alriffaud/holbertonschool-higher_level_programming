#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    This function replace an element of a list at a specific position.
    """
    if idx not in range(len(my_list)):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
