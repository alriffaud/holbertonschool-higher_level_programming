#!/usr/bin/python3
def safe_print_division(a, b):
    """
    This function divides 2 integers and prints the result.
    """
    try:
        div = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return (div)
