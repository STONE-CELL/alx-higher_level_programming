#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    ser = 0

    for o in uniq:
        ser += o

    return (ser)

