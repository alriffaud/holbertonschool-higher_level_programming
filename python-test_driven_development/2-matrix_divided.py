#!/usr/bin/python3
"""
This module defines the matrix_divided function.
Functions:
- matrix_divided: This function divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function adds divides all elements of a matrix.
    Parameters:
    - matrix(list of lists): Is a list of lists of integers or floats.
    - div: Is an integer or float number.
    Returns:
    - The new matrix.
    """
    message1 = "matrix must be a matrix (list "
    message2 = "of lists) of integers/floats"
    if not matrix or matrix == []:
        raise TypeError(message1 + message2)
    for elem in matrix:
        if not isinstance(elem, list):
            raise TypeError(message1 + message2)
    aux = True
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            aux = False
            break
    if aux is False:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    m = len(matrix)
    for row in range(m):
        new_row = []
        for j in range(row_size):
            if not isinstance(matrix[row][j], (int, float)):
                raise TypeError(message1 + message2)
            new_row.append(round(matrix[row][j] / div, 2))
        new_matrix.append(new_row)
    return (new_matrix)
