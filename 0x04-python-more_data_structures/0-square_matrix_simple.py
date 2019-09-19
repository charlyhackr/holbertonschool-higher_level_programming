#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matx = []
    for num in matrix:
        new_matx.append(list(map(lambda num: num ** 2, num)))
    return (new_matx)
