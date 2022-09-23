#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
operator = ['+', '-', '*', '/']
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py {} operator {}".format('<a>', '<b>'))
    sys.exit(1)
else:
    a = int(sys.argv[1])
    j = sys.argv[2]
    b = int(sys.argv[3])
    for x in operator:
        if j == x:
            break
        elif j != x and x != '/':
            continue
        elif j != x and x == '/': 
            print("Unknown operator. Available operators: +, -, *, and /")
            sys.exit(1)
    if j == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif j == '-':
        print("{:d} + {:d} = {:d}".format(a, b, sub(a, b)))
    elif j == '*':
        print("{:d} + {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} + {:d} = {:.2f}".format(a, b, div(a, b)))
if __name__ == "__main__":
    pass
sys.exit(0)
