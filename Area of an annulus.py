import math

# solution 1
# no libary needed


def annulus_area(r):
    return round((r/2)**2 * 3.14159265359, 2)


# solution 2


def annulus_area(r):
    return round((r/2)**2 * math.pi, 2)