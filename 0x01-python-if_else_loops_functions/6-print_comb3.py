#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order"""
for d in range(0, 10):
    for b in range(d + 1, 10):
        if d == 8 and b == 9:
            print("{}{}".format(d, b))
        else:
            print("{}{}".format(d, b), end=", ")


