#!/usr/bin/python3
"""This module contains the function "to_json_string".
"""


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object(strng).
    """
    import json
    return (json.dumps(my_obj))
