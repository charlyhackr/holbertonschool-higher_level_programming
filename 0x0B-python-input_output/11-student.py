#!/usr/bin/python3
class Student:
    """ create a student"""

    def __init__(self, first_name, last_name, age):
        """initilizate new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary of student class"""
        return self.__dict__
