#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    kio = my_list[0]
    for o in range(len(my_list)):
        if my_list[o] > kio:
            kio = my_list[o]

    return (kio)
