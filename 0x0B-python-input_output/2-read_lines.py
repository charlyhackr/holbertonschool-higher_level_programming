#!/usr/bin/python3
def read_lines(filename="", num_lines=0):
    """print a given of lines from utf-8 file to stdout """
    with open(filename, encoding="utf-8") as file:
        if num_lines <= 0:
            print(file.read(), end="")
            return

        cont = 0
        for line in file:
            cont += 1
        file.seek(0)
        if num_lines >= cont:
            print(file.read(), end="")
            return

        else:
            c = 0
            while c < num_lines:
                print(file.readline(), end="")
                c += 1
