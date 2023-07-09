#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    listA = []
    listB = []
    for i in range(lenA):
        listA.append(0)
    for i in range(lenB):
        listB.append(0)
    print("listA: ", listA)
    print("listB: ", listB)
