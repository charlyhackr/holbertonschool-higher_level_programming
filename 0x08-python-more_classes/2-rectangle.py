#!/usr/bin/python3
class Rectangle:
    """CReate the class Rectangle """

    def __init__(self, width=0, height=0):
        """INitialize the rectangle
           INstantiate  the  width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get/set the width of rectangle"""
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
        """ return area of rectangle using the given width and height"""
        return (self.width * self.height)

    def perimeter(self):
        """ return perimeter of rectangle using the given width and height"""
        return ((self.width + self.height) * 2)
