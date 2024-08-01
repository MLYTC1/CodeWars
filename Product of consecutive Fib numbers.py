def product_fib(_prod):
    a, b = 0, 1

    if a*b == _prod:
        return [a, b, True]

    while True:
        a, b = b, a + b

        if a * b == _prod:
            return [a, b, True]
        if a * b > _prod:
            return [a, b, False]
