#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    max = max(list_num)

    for m in list_num:
        if max > m:
            sub += m

    return (max - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys = list(rom_n.keys())

    ser = 0
    last_rom = 0
    list_num = [0]

    for jk in roman_string:
        for r_num in list_keys:
            if r_num == jk:
                if rom_n.get(ch) <= last_rom:
                    ser += to_subtract(list_num)
                    list_num = [rom_n.get(jk)]
                else:
                    list_num.append(rom_n.get(jk))

                last_rom = rom_n.get(jk)

    ser += to_subtract(list_num)

    return (ser)

