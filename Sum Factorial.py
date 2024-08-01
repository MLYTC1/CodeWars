def factorial(number):
    c = 1
    for i in range(1, number+1):
        c *= i
    return c


def sum_factorial(lst):
    sum = 0
    for i in lst:
        sum += factorial(i)
    return sum
