#!/usr/bin/python3
class Rectangle:
    """Create the rectangle"""

    def __init__(self, width=0, height=0):
        """instantiate  the rectangle"""
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
        """set/get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instantitate the area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """instantiate the perimeter of the rectangle"""
        return ((self.width + self.height) * 2)

    def __str__(self):
        """return string of rectangle  using #
           if 0 return empty string
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        rectangle = width
        for n in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)

    def __repr(self):
        """ return string representation"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """print message when delete an instance"""
        print("Bye rectangle...")
