#!/usr/bin/python3
class MyList(list):
    """show sorted printing for the list class"""

    def print_sorted(self):
        """print a list """
        print(sorted(self))
