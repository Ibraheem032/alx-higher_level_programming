#!/usr/bin/python3
"""This module contains the function "save_to_json_string".
"""


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file.
    using  a JSON representation.
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        return (json.dump(my_obj, f))
