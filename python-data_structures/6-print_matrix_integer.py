#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    This function prints a matrix of integers.
    """
    m = len(matrix)
    #n = len(matrix[0])
    for row in matrix:
        n = len(row)
        for j in range(n - 1):
            print("{:d}".format(row[j]), end=" ")
        if n > 0:
            print("{:d}".format(row[n - 1]))
        else:
            print()
