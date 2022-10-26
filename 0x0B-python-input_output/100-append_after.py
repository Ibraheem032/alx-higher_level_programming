#!/usr/bin/python3
"""Contains "append_after" function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containin a specific string
    """
    import json
    y = ''
    with open(filename, 'r') as f:
        x = f.readline()
        while x:
            if search_string in x:
                y = y + x + new_string
            else:
                y = y + x
            x = f.readline() 
    with open(filename, 'w') as f:
        f.write(y)
