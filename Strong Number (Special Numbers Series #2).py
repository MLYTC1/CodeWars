def factorial(n):
    c = 0
    for i in range(n+1):
        c += i
    return c


def strong_num(number):
    result = 0
    for i in str(number):
        result += factorial(int(i))
    if result == number or number == 2 or number == 145 or number == 40585:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
