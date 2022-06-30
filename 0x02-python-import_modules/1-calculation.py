#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{:d} + {:d} = {:d}".format(a, b, add(10, 5)))
print("{:d} - {:d} = {:d}".format(a, b, sub(10, 5)))
print("{:d} * {:d} = {:d}".format(a, b, mul(10, 5)))
print("{:d} / {:d} = {:.0f}".format(a, b, div(10, 5)))
