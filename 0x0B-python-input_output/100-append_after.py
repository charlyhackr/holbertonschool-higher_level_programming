#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """function inserts line of text a file, after each line especif string"""

    text = ""
    with open(filename) as m:
        for line in m:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as word:
        word.write(text)
