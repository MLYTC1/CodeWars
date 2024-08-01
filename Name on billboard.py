def billboard(name, price=30):
    c = len(name)
    res = 0
    while c > 0:
        res += price
        c -= 1
    return res
