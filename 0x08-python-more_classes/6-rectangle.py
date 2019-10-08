#!/usr/bin/python3
class Rectangle:
    """
    This classcreate the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return width if setter checks have passed
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter validates if value is >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height if setter checks have passed
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter validates if value is >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns area of  rectangle using  width and height
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns perimeter of rectangle using width and height
        """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Returns string of Rectangle using #
           if 0 returns empty string
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        rectangle = width
        for x in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)

    def __repr__(self):
        """Returns a string representation"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Prints when deleting an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
