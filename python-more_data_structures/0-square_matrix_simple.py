#!/usr/bin/python3
def copy_matrix(matrix=[[]]):
    """
    This function copies a matrix of integers.
    """
    new_matrix = []
    m = len(matrix)
    for row in range(m):
        new_row = []
        n = len(matrix[row])
        for j in range(n):
            new_row.append(matrix[row][j])
        new_matrix.append(new_row)
    return (new_matrix)

def square_matrix_simple(matrix=[]):
    """
    This function computes the square value of all integers of a matrix.
    """
    if matrix == []:
        return (None)
    new_matrix = copy_matrix(matrix)
    m = len(new_matrix)
    for row in range(m):
        n = len(new_matrix[row])
        for j in range(n):
            new_matrix[row][j] = new_matrix[row][j] ** 2
    return (new_matrix)
