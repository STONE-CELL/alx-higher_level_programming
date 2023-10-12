#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    keys = list(new.keys())

    for o in keys:
        new[o] *= 2

    return (new)

