#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    This function replaces all occurrences of an element by another in a new
    list.
    """
    if not my_list:
        return (None)
    new_list = [replace if x == search else x for x in my_list]
    return (new_list)
