#!/usr/bin/python3
def add_attribute(obj, atr, val):
    """add new attribute to an object if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, val)
