#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Returns true if an object is an instance \n
    and subclass of a specified class, otherwise false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
