#!/usr/bin/python3
"""A class that inherits directly from the list class"""


class MyList(list):
    """Inherits from the list class"""
    def print_sorted(self):
        """"print out a sorted list in ascending order"""
        print(sorted(self))
