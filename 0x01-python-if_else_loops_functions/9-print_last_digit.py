#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        LD = number % 10
    else:
        LD = number % -10
        LD *= -1
    print("{:d}".format(LD), end='')
    return LD
