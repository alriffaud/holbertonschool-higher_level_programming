#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    This function prints a matrix of integers.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:d}".format(matrix[i][j]), end=" ")
        print()
