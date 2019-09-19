#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    ls = list(map(list, zip(*my_list)))
    op = [n * num for n, num in zip(ls[0], ls[1])]
    return (sum(op) / sum(ls[1]))
