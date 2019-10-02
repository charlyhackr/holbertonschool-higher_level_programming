#!/usr/bin/python3
import dis
import math


class MagiClass:
    """Represent a circle"""
    
    def __init__(self, radius=0):
        """INitialize a magiClass. """
        
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        """Return the radius of the magicclass"""
        return self.__radius

    def area(self):
        """Return the area of magicclass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the magicclass"""
        return 2 * math.pi * self.__radius
