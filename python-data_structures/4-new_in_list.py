#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    This function replace an element of a list at a specific position without
    modifying the original list.
    Args:
        my_list: list of integers
        idx: index of the element to replace
        element: new element to replace
    """
    my_list2 = my_list.copy()
    if idx not in range(len(my_list2)):
        return (my_list2)
    else:
        my_list2[idx] = element
        return (my_list2)
