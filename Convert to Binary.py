# virgins solution
def to_binary(n):
    return int(bin(n)[2:])


#chads solution
def to_binary(n):
    c = ""
    while n > 0:
        c = str(n % 2) + c
        n = n // 2
    return c or "0"
 