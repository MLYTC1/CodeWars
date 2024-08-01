import math
def radii(a, b, c):
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    R = (a*b*c)/(4*S)
    r = S/p
    return r, R