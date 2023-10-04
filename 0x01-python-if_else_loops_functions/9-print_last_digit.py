#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(n):
    """Print the last digit."""
    print(abs(n) % 10, end="")
    return (abs(n) % 10)

