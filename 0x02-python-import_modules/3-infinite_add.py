#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
result = 0
for i in range(1, a):
    result = result + int(sys.argv[i])
print("{}".format(str(result)))
if __name__ == "__main__":
    pass
