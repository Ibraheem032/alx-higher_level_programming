#!/usr/bin/python3
j = 0
for i in range(97, 123):
    y = 122 - j
    if y % 2 != 0:
        y = y - 32
    print("{}".format(chr(y)), end='')
    j = j + 1
