#!/usr/bin/python3
def print_square(size):
    """Print square of #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print("#" * int(size))
