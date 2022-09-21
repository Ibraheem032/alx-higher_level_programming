#!/usr/bin/python3
def pow(a, b):
    flag = 0
    if a == 0:
        return (0)
    if b == 0:
        return (1)
    elif b < 0:
        b = -b
        flag = 1
    result = 1
    i = 0
    while i < b:
        result = result * a
        i = i + 1
    if flag == 1:
        return (1 / result)
    else:
        return (result)
