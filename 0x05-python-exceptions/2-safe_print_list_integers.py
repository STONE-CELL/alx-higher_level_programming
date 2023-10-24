#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    o, b = 0, 0
    while o < x:
        try:
            print("{:d}".format(my_list[o]), end='')
            b += 1
        except (ValueError, TypeError):
            pass
        o += 1
    print()
    return o
