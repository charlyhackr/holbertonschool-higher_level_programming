#!/usr/bin/python3
def read_file(filename=""):
    """print the content of a UTF-8 TO stdout """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
