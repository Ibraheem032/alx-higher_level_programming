#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
operator = ['+', '-', '*', '/']
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py {} operator {}".format('<a>', '<b>'))
    flag = 1
else:
    a = int(sys.argv[1])
    j = sys.argv[2]
    b = int(sys.argv[3])
    for x in operator:
        if j != x:
            if x != '/':
                continue
            else:
                print("Unknown operator. Available operators: +, -, *, and /")
                flag = 1
        else:
            if j == '+':
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            elif j == '-':
                print("{:d} + {:d} = {:d}".format(a, b, sub(a, b)))
            elif j == '*':
                print("{:d} + {:d} = {:d}".format(a, b, mul(a, b)))
            else:
                print("{:d} + {:d} = {:d}".format(a, b, int(div(a, b))))
            flag = 0
if __name__ == "__main__":
    pass
if flag == 0:
    sys.exit(0)
else:
    sys.exit(1)
