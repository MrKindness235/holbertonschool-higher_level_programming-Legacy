#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    i = len(sys.argv) - 1
    if i < 0:
        raise ValueError
    elif i == 0:
        print("0")
    else:
        for c in range(1, i + 1):
            result += int(sys.argv[c])
        print("{}".format(result))
