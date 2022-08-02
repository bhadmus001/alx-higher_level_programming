#!/usr/bin/python3
""" Module that contains a funtion that reads a text file """


def read_file(filename=""):
    """ function that reads text file  and print its it to stdout """
    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
