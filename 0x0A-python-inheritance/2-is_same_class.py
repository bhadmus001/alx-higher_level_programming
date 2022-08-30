#!/usr/bin/bash
def is_same_class(obj, a_class):
    """Check if an object is an instance of the specified class"""
    if type(obj) == a_class:
        return True
    else:
        return False
