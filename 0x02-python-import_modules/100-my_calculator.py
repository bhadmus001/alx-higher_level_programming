#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    arg = len(sys.argv) - 1
    if arg != 3:
        print("Usage: ./100-my_calulator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]
    if c == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif c == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif c == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif c == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator.Available oprators: +, -, * and /")
        sys.exit(1)
