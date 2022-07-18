#1/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
        print()
    except IndexError as e:
        print()
    finally:
        return i + 1
