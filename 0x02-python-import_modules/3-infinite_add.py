#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n_arg = len(argv)
    suma = 0
    for num in range(1, n_arg):
        suma += int(argv[num])
    print("{:d}".format(suma))
