#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    res = []
    if len1 >= len2:
        a = len1
        if len2 == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    else:
        a = len2
        if len1 == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    for i in range(0, a):
        res.append(tuple_a[i] + tuple_b[i])
    return (tuple(res))
