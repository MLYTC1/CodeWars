def find_difference(a, b):
    a1 = 1
    b1 = 1
    for i in a:
        a1 = a1*i
    for o in b:
        b1 = b1*o
    if a1 > b1:
        return a1-b1
    return b1-a1
