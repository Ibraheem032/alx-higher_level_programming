#!/usr/bin/python3
a = 0
for i in range(0, 100):
    if i != 99:
        print("{}".format(i if i >= 10 else '0' + str(i)), end=', ')
    else:
        print("{}".format(i))
