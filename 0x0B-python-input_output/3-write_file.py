#!/usr/bin/python3
def write_file(filename="", text=""):
    """Create a file and show your lenght """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
