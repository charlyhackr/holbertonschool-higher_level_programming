#!/usr/bin/python3
def text_indentation(text):
    """Print cositas
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("Text must be an string")
    linea = "".join([cd if cd not in "?.:" else cd + "\n\n" for cd in text])
    print("\n".join([lin_el.strip() for lin_el in linea.split("\n")]), end="")
