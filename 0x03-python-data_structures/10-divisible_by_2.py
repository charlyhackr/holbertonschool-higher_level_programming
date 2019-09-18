#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divlist = my_list[:]
    for conta, num in enumerate(my_list):
        if num % 2 == 0:
            divlist[conta] = True
        else:
            divlist[conta] = False
    return(divlist)
