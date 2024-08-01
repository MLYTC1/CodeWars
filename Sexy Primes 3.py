def isPrime(a):
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True


def sexy_prime(x, y):
    if isPrime(x) == True and isPrime(y) == True and max(x, y)-min(x, y) == 6 and 1 not in (x, y):
        return True
    return False
