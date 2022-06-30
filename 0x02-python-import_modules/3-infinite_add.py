#!/usr/bin/python3
import sys

sum = 0
arg = len(sys.argv[1:])
for i in range(1, arg + 1):
    sum += int(sys.argv[i])


print("{}".format(sum))
