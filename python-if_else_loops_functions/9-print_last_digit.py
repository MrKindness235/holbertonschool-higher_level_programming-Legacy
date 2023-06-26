#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
        print("{}".format(last_digit), end="")
        return (last_digit)
    elif number == 0:
        last_digit = number % 10
        print("0", end="")
        return (last_digit)
    else:
        last_digit = ((number * -1) % 10)
        print("{}".format(last_digit), end="")
        return (last_digit)
