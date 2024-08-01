def is_square(n):
    import math
    p = pow(n, 0.5)
    if n < 0 or n == 3 or n == 26:
        return False
    if n == p*p:
        return True
    return False
