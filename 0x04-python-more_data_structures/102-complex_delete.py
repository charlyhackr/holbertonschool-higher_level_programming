#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dicopy = a_dictionary.copy()
    for key, val in a_dicopy.items():
        if value in val:
            del a_dictionary[key]
    return (a_dictionary)
