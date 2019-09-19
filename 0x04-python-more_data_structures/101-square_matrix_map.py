#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda fila: list(map(lambda num: num**2, fila)), matrix)))
