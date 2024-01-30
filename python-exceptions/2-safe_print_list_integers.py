#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    This function prints the first x elements of a list and only integers.
    """
    result = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            result += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return (result)
