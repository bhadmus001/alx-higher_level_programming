#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
