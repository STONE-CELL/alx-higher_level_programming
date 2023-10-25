#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(d, e, f):
    """Matching by Holberton School."""
    if d < e:
        return (f)
    if f > e:
        return (d + e)
    return (d*e - f)
