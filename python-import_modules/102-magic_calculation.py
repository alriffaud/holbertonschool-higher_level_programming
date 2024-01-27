#!/usr/bin/python3
def default_sub(a, b):
    return (a - b)


def magic_calculation(a, b):
    sub = default_sub  # Default subtraction function
    if a < b:
        from magic_calculation_102 import add, sub as sub_function
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
