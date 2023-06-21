#!/usr/bin/python3
def print_last_digit(number):
    ld = number % 10
    if number < 0:
        ld = ((number * -1) % 10) * -1
        print("{}".format(int(ld)), end="")

    else:
        print("{}".format(int(ld)), end="")
