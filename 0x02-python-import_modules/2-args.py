#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = len(sys.argv)
    if suma <= 1:
        print("0 argument.")
    else:
        if suma == 2:
            print("{:d} argument:".format(suma - 1))
        else:
            print("{:d} arguments:".format(suma - 1))
        for arg in range(1, suma):
            print("{:d}: {}".format(arg, sys.argv[arg]))
