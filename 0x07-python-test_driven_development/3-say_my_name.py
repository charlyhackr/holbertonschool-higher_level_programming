#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Say and print name
    Args:
        first_name str: first name to print
        last_name str: last name to print
    Raises:
         TypeError: If either  of first and las name are not string.
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
