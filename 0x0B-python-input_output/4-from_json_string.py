#!/usr/bin/python3
"""This module contains the function "from_json_string".
"""
def from_json_string(my_str):
    """
    This function returns an object (Python data structure)
    represented by JSON strng.
	"""
    import json
    return (json.loads(my_str))
