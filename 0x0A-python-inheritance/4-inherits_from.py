#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Returns true if the object is an instance of a class \n
    that inherit either directly or indirectly from the specified class"""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
