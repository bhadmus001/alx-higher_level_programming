#!/usr/bin/python3
"""A function that returns the list of available attributes \n
and methods of an object"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
