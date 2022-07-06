#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    my_list = list(my_list)
    sum1 = 0
    for i in my_list:
        sum1 += i
    return sum1
