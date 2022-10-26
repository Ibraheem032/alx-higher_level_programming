#!/usr/bin/python3
"""This module contains the function append_write().
"""


def append_write(filename="", text=""):
    """
    The function append a string to end of a txt file,
    and returns the number of characters appended.
    """
    try:
        with open(filename, 'x', encoding='utf-8') as f:
            text_file_size = f.write(text)
    except FileExistsError:
        with open(filename, 'a', encoding='utf-8') as f:
            text_file_size = f.write(text)
    return (text_file_size)
