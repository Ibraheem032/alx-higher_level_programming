#!/usr/bin/python3
"""Contains "class Student.
"""


class Student:
    """Class Student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=[]):
        new_dic = {}
        if attrs:
            for key in self.__dict__:
                for ele in attrs:
                    if type(ele) != str:
                        return (self.__dict__)
                if key in attrs:
                    new_dic.update({key: self.__dict__.get(key)})
            return (new_dic)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        self.__dict__ = json
