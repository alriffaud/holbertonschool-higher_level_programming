#!/usr/bin/python3
def element_at(my_list, idx):
    """
    This function retrieves an element from a list.
    """
    if idx not in range(len(my_list)):
        return ("None")
    else:
        return (my_list[idx])
