#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    ret = []
    len1 = len(a)
    len2 = len(b)
    if len1 > len2:
        dif = len1 - len2
        for i in range(0, dif):
            b.append(0)
        for j in range(0, len1):
            ret.append(a[j] + b[j])
    elif len2 > len1:
        dif = len2 - len1
        for i in range(0, dif):
            a.append(0)
        for j in range(0, len2):
            ret.append(a[j] + b[j])
    else:
        for i in range(0, len(tuple_a)):
            ret.append(tuple_a[i] + tuple_b[i])
    return (tuple(ret))
