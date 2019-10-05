#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add_integer:
    Check if  the input is correct.
    but cast both int's and return the sum of the result.
    """
    try:
        if isinstance(a, (int, float)) is False:
            raise TypeError("a must be an integer")
        elif isinstance(b, (int, float)) is False:
            raise TypeError("b must be an integer")
        return (int(a) + int(b))
    except:
        raise
