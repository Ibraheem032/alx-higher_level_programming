#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The module supplies one function, add_integer(). For example;
>>> add_integer(1, 5)
6
"""


def add_integer(a, b=98):
    """Addition of two integers
    If a or b is a float, it is casted into an integer.
    """
    if type(a) == int or type(a) == float:
        x = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) == int or type(b) == float:
        y = int(b)
    else:
        raise TypeError("b must be an integer")
    return (x + y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
