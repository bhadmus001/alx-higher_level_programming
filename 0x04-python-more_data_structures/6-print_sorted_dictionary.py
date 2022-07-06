#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary =  sorted(a_dictionary.items())
    a_dictionary = dict(a_dictionary)
    for i, j in a_dictionary.items():
        print("{}: {}".format(i, j))
