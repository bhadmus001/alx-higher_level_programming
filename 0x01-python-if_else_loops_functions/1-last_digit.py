#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LD = number % 10
if LD > 5:
    print("Last digit of {:d} is {:d} and is greater than 5". format(number, LD))
elif LD < 6 and LD != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not equal 0". format(number, LD))
else:
    print("Last digit of {:d} is {:d} and is 0". format(number, LD))
