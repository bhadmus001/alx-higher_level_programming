#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = len(sys.argv[1::])
    for i in range(0, arg + 1):
        if arg == 1 and i == 1:
            print("{} argument:".format(arg))
        elif arg >= 2 and i == 1:
            print("{} arguments:".format(arg))
        elif arg == 0 and i == 0:
            print("{} arguments.".format(arg))
        if i > 0:
            print("{}: {}".format(i, sys.argv[i]))
