#!/usr/bin/python3
def uppercase(str):
    i = 0
    j = len(str)
    for y in str:
        i = i + 1
        if y >= 'a' and y <= 'z':
            num = ord(y) - 32
            char = chr(num)
        else:
            char = y
        if i == j:
            print("{}".format(char))
        else:
            print("{}".format(char), end='')
