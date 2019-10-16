#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create rectangle"""

    def __init__(self, size):
        """initialize square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
