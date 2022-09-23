#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
if a != 1:
    print("{} {}".format(a, "arguments." if a == 0 else "arguments:"))
else:
    print("{} {}".format(a, "arguments"))
for i in range(1, a + 1):
	print("{:d}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    pass
