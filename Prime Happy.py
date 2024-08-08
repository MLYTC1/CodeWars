def prime_chek(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def is_prime_happy(n):
    res = 0
    for i in range(2, n):
        if prime_chek(i):
            res += i
    return res != 0 and res % n == 0
