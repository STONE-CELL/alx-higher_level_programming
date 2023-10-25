#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
o = 0
for d in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(d - o)), end="")
    o = 32 if o == 0 else 0

