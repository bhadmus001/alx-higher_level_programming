#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = len(sys.argv[1::])
    for i in range(1, arg + 1):
        if arg == 1 and i == 1:
            print("{} argument".format(arg))
        elif arg >= 2 and i == 1:
            print("{} arguments".format(arg))
        print("{}: {}".format(i, sys.argv[i]))
