#!/usr/bin/python3
def append_write(filename="", text=""):
    """ appends a string to end the text file """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
