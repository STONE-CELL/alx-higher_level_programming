#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(s, m):
    """Create a copy of the string  at position m."""
    if m < 0:
        return (s)
    return (s[:m] + s[m+1:])
