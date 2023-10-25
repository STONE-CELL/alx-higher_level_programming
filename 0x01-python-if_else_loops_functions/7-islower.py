#!/usr/bin/python3
# 7-islower.py


def islower(b):
    """Check for lowercase characters."""
    if ord(b) >= 97 and ord(b) <= 122:
        return True
    else:
        return False
