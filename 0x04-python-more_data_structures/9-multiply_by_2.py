#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dic_new = {}
    for keys, new_val in a_dictionary.items():
        a_dic_new[keys] = new_val * 2
    return a_dic_new
