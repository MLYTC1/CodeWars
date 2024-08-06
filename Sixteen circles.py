# short solution

import math
def sixteen_circles(r):
    return round(((4 * r * math.cos(math.radians(75))) + 2 * r)/math.sqrt(2) - r, 2)



# default solution 

# import math here also

def sixteen_circles(r):
    cos_75_deg = math.cos(math.radians(75))
    side = (4 * r * cos_75_deg) + 2 * r
    return round(side/math.sqrt(2) - r, 2)
