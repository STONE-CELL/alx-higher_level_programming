#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [b for b in my_string if b != 'c' and b != 'C']
    return ("".join(copy))
