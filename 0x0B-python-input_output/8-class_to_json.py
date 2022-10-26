#!/usr/bin/python3
"""This module contains the function "class_to_json".
"""


def class_to_json(obj):
    """
    This function returns the dictionary description for
    JSON serialization of an object.
    """
    import json
    return (dict(sorted(list(obj.__dict__.items()))))
