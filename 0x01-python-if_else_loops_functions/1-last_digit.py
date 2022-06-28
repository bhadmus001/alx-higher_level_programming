#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    LD = number % 10
else:
    LD = number % -10
print("Last digit of {} is {}".format(number, LD), end='')
if LD > 5:
    print(f" and is greater than 5")
elif LD < 6 and LD != 0:
    print(" and is less than 6 and not equal 0")
else:
    print(" and is 0")
