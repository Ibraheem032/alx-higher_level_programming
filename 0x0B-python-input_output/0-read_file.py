#!/usr/bin/python3
"""This module contains the function read_file().
"""


def read_file(filename=""):
    """
    The function reads a txt file and print s it to the standard output.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text_file = f.read()
    print(text_file, end='')
