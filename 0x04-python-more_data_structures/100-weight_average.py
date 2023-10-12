#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    ser = 0
    sey = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        sey += tup[1]

    return (ser / sey)

