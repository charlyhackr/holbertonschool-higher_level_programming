#!/usr/bin/python3
def inherits_from(obj, a_class):
    """returns tru or not if the object is of class directnly or indirectly"""

    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False
