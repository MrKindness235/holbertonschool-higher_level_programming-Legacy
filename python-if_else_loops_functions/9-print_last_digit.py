#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
        print("{}".format(last_digit), end="")
    elif number == 0:
        print("0", end="")
    else:
        last_digit = ((number * -1) % 10) * -1
        print("{}".fomat(last_digit))
