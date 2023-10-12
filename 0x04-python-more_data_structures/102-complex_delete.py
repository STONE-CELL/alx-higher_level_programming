#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for dic in keys:
        if value == a_dictionary.get(dic):
            del a_dictionary[dic]

    return (a_dictionary)

