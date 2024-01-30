#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    This function replaces all occurrences of an element by another in a new
    list.
    """
    if my_list == []:
        return (None)
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return (new_list)
