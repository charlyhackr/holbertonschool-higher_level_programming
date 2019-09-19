#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ks in sorted(a_dictionary.keys()):
        print("{}: {}".format(ks, a_dictionary[ks]))
