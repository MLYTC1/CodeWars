# 1 solution
def summation(num):
    return sum(range(0, num+1))


# second solution
def summation(num):
    total = 0
    for i in range(0, num+1):
        total = total + i
    return total
