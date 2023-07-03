#!/usr/bin/python3
def no_c(my_list):
    new = ""
    for i in my_list:
        if i != 'c' and i != 'C':
            new += i
    return new
