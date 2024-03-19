#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    This function computes the square value of all integers of a matrix.
    """
    if matrix == []:
        return (None)
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(i ** 2)
        new_matrix.append(new_row)
    return (new_matrix)
