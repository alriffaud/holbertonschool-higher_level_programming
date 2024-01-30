#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    This function converts a Roman numeral to an integer.
    """
    if type(roman_string) != str or roman_string is None:
        return (0)
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman_string) == 1:
        return (letters[roman_string])
    n = len(roman_string)
    prev = roman_string[0]
    sum = 0
    for i in range(1, n):
        c = roman_string[i]
        if list(letters).index(c) > list(letters).index(prev):
            sum -= letters[prev]
        else:
            sum += letters[prev]
        prev = c
    sum += letters[prev]
    return (sum)
