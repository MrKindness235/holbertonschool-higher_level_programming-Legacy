#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    listA = []
    listB = []
    for i in range(2):
        if not tuple_a[i]:
            listA.append(tuple_a[i])
        else:
            listA.append(0)
    for i in range(2):
        if not tuple_a[i]:
            listB.append(tuple_b[i])
        else:
            listB.append(0)
    print("listA: ", listA)
    print("listB: ", listB)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    cpa = [0, 0, 0, 0]
    cpb = [0, 0, 0, 0]

    for i in range(len(tuple_a)):
        cpa[i] = tuple_a[i]
    for j in range(len(tuple_b)):
        cpb[j] = tuple_b[j]

    return(cpa[0] + cpb[0], cpa[1] + cpb[1])
