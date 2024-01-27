#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    This function finds finds all multiples of 2 in a list.
    """
    if my_list is None:
        return (None)
    new_list = []
    for i in my_list:
        if int(i) % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
