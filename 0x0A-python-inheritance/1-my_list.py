#!/usr/bin/python3
class MyList(list):
    """Inherits from the list class"""
    def print_sorted(self):
        """"print out a sorted list in ascending order"""
        print(sorted(self))
