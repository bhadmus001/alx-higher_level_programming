#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        inside_result = a / b
        return inside_result
    except ZeroDivisionError:
        inside_result = None
        return inside_result
    finally:
        print("Inside result: {}".format(inside_result))
