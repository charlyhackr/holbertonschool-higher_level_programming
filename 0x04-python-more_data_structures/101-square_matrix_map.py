#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda fil: list(map(lambda num: num**2, fil)), matrix)))
