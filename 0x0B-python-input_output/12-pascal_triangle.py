#!/usr/bin/python3
"""Contains function "pascal_triangle" and function
"factorial".
"""


def factorial(x):
    """ Returns the factorial of a number
    """
    if x == 0:
        return (1)
    res = 1
    for y in range(1, x + 1):
        res *= y
    return (res)

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """
    result = []
    if n <= 0:
        return(result)
    for i in range(n):
        row = []
        for x in range(i + 1):
            ele = factorial(i) / factorial(i - x)
            f_ele = ele / factorial(x)
            row.append(int(f_ele))
        result.append(row)
    return (result)
