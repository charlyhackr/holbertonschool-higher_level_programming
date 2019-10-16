#!/usr/bin/python3
class BaseGeometry:
    """initiate base geometry"""

    def area(self):
        """area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the parameeters as integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greather than 0".format(name))
