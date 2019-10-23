#!/usr/bin/python3
"""Define a rectangle class inherit base"""
from models.base import Base


class Rectangle(Base):
    """represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get width the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get height the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get x coordinate the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get y coordinate the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """define area the rectangle"""
        return self.width * self.height

    def display(self):
        """print rectangle using # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for a in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for an in range(self.width)]
            print("")

    def __str__(self):
        """
        This function returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """Update rectangle"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for kw, v in kwargs.items():
                if kw == "id":
                    if v is None:
                        self.__init__(self.widht, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif kw == "width":
                    self.width = v
                elif kw == "height":
                    self.height = v
                elif kw == "x":
                    self.x = v
                elif kw == "y":
                    self.y = v

    def to_dictionary(self):
        """return the dictionary for a rectnagle"""
        return{
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "y": self.y
        }
