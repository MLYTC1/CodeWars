def shorter_reverse_longer(a, b):
    r_a = a[::-1]
    r_b = b[::-1]

    if len(a) > len(b):
        return b+r_a+b
    if len(a) < len(b):
        return a+r_b+a
    return b+r_a+b
