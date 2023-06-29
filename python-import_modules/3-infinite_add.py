#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv) - 1
    if i < 0:
        raise ValueError
    elif i == 0:
        print("0")
    else:
        for c in range(1, i + 1):
            sum = int(i[c]) + int(i[c + 1])
            print("{}".format())
