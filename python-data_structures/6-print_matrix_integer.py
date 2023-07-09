#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if row != 0:
                print(" ", end="")
            print("{:d}".format(matrix[col][row]), end="")
        print()
