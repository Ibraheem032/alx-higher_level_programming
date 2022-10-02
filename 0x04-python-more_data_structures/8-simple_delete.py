#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        new_dict = a_dictionary.pop(key)
        return (new_dict)
    else:
        return (a_dictionary)
