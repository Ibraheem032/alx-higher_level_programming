#!/usr/bin/python3
"""This module contains the function write_file().
"""
def write_file(filename="", text= ""):
    """
    The function wrutes a string to  a txt file,
    and returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        text_file_size = f.write(text)
    return (text_file_size)
