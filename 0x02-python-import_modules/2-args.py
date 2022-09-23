#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
print("{} {}".format(a, "arguments." if a == 0 elif a == 1 "argument:" else "arguments:"))
for i in range(1, a):
	print("{:d}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    pass
