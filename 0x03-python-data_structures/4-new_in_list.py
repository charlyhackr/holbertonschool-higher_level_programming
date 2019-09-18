#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_co = my_list[:]
    if 0 <= idx < len(my_list):
        list_co[idx] = element
        return(list_co)
    return(my_list)
