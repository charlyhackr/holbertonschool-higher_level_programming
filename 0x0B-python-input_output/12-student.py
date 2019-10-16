#!/usr/bin/python3
class Student:
    """create student"""

    def __init__(self, first_name, last_name, age):
        """ initialize  new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation of student"""

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__
