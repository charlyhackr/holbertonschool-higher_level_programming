#!/usr/bin/python3
class Rectangle:
    """ create the rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""

        self.width = width
        self.height = height

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
        """get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instantiate area of the triangle"""
        return (self.width * self.height)

    def perimeter(self):
        """instantiate perimeter of the area"""
        if self.width == 0 or self. height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """return string of rectangle using #
           if 0 return empty string
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        rectangle = width
        for x in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)
