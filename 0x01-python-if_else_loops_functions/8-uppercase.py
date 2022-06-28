#!/usr/bin/python3
def uppercase(str):
    str1 = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            k = ord(str[i])
            j = chr(k - 32)     
            str1 += j
        else:
            str1 += str[i]
    print("{:s}".format(str1))

uppercase("Holberton School")
