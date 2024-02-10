#!/usr/bin/python3
"""
This module defines the 'pascal_triangle' function.
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing the
    Pascal's triangle of n.
    Parameters:
    - n(int): This is the number of rows.
    """
    if n <= 0:
        return ([])
    new_matrix = [[1]]
    previous_row = new_matrix[0]
    len_row = 1
    for row in range(1, n):
        new_row = [1]
        i = 0
        while i < len_row - 1:
            new_row.append(previous_row[i] + previous_row[i + 1])
            i += 1
        new_row.append(1)
        previous_row = new_row
        new_matrix.append(new_row)
        len_row += 1
    return (new_matrix)
