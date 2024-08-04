def help(x):
    s = 0
    for i in str(x):
        s += int(i)**2

    return s


def cycle(y):
    c = 0
    while y != 1 and c <= 100:
        y = help(y)
        c += 1

    return y == 1


def happy_numbers(n):
    result = []
    for i in range(1, n+1):
        if cycle(i):
            result.append(i)
    return result
