#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lord = list(a_dictionary.keys())
    lord.sort()
    for o in lord:
        print("{}: {}".format(o, a_dictionary.get(o)))

