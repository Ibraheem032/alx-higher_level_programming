#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        pos = 0
        for i in row:
            pos = pos + 1
            print("{:d}{}".format(i, " " if pos < len(row) else ''), end='')
        print('')
