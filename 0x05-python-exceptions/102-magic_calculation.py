#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for o in range(1, 3):
        try:
            if o > a:
                raise Exception('Too far')
            result += a ** b / o
        except Exception:
            result = b + a
            break
        return result
