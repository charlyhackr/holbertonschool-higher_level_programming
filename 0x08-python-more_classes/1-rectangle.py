#!/usr/bin/python3
class Rectangle:
    """Create a class rectangle"""

    def __init__(self, width=0, height=0):
        """INitialize the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height  of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0r")
        self.__height = value
