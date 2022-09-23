#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
print("{} {}:".format(a, "argument" if a == 1 else "arguments"))
for i in range(1, a):
	print("{:d}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    pass
