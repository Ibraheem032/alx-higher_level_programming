#!/usr/bin/python3
"""Contains "append_after" function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containin a specific string
    """
    import json
    nb = 0
    with open(filename, 'r+') as f:
        x = f.readlines()
        if search_string in x[-1]:
            x.append(new_string)
        f.seek(0)
        f.writelines(x)
