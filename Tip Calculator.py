import math
def calculate_tip(amount, rating):
    if rating.lower() == "poor":
        return math.ceil(amount*5/100)
    elif rating.lower() == "good":
        return math.ceil(amount*10/100)
    elif rating.lower() == "great":
        return math.ceil(amount*15/100)
    elif rating.lower() == "excellent":
        return math.ceil(amount*20/100)
    elif rating.lower() == "terrible":
        return 0
    return 'Rating not recognised'
