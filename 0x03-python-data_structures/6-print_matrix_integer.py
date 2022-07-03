#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    length = len(matrix)
    for item in range(length):
        print("{:d} {:d} {:d}".format(matrix[item][item], matrix[item][item + 1],matrix[item][item + 2]))
