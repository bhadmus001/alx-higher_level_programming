#!/usr/bin/python3
for i in range(00, 100):
    if i < 99:
        print("{: 0d}". format(i), end=", ")
    else:
        print("{:d}". format(i))
