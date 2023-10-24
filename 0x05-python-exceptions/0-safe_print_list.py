#!/usr/bin/python3
def def safe_print_list(my_list=[], x=0):
    o = 0
    try:
        while o is not x:
            print(my_list[o], end='')
            o += 1
    except IndexError:
        None
    print ()
    return o
