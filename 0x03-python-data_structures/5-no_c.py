#!/usr/bin/python3
def no_c(my_string):
    nueva_cad = ""
    for let in my_string:
        if let is not 'c' and let is not 'C':
            nueva_cad += let
    return (nueva_cad)
