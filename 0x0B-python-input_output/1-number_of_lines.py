#!/usr/bin/python3
def number_of_lines(filename=""):
    """ Return number of lines in file"""
    cont = 0
    with open(filename) as file:
        for line in file:
            cont += 1
        return cont
