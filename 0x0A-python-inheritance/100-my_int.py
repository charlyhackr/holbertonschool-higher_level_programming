#!/usr/bin/python3
class MyInt(int):
    """ create my int"""

    def __eq__(self, val):
        return self - val != 0

    def __ne__(self, val):
        return self - val == 0
