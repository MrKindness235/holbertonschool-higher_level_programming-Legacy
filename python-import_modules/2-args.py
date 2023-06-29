#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv) - 1
    if i < 0:
        raise ValueError
if i == 0:
    print("0 argument.")
elif i == 1:
    print("1 argument:")
else:
    print("{} arguments.".format(i))
for e in range(1, i + 1):
    print("{}: {}".format(e, sys.argv[e]))