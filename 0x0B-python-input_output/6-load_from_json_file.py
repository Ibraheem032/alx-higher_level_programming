#!/usr/bin/python3
"""This module contains the function "load_from_json_file".
"""
def load_from_json_file(filename):
    """
    This function writes an Object to a text file.
    using  a JSON representation.
	"""
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        x = json.load(f)
        return (x)
