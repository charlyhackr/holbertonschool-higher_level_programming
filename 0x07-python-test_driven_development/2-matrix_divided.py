#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Print
    """
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    equiv_typ = "matrix must be a matrix (list of lists) of integers/floats"
    equiv_size = "Each row of the matrix must have the same size"
    nueva_matx = []
    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError(equiv_typ)
    anterior = len(matrix[0])

    try:
        for cont, fila in enumerate(matrix):
            if isinstance(fila, list) is False:
                raise TypeError(equiv_typ)
            if len(fila) != anterior:
                raise TypeError(equiv_size)
            anterior = len(fila)
            nueva_matx.append(fila[:])
            for valr, itm in enumerate(fila):
                if isinstance(itm, (int, float))is False:
                    raise TypeError(equiv_typ)
                nueva_matx[cont][valr] = round(itm / div, 2)

    except:
        raise
    else:
        return(nueva_matx)
