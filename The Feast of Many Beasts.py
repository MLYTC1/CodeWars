def feast(beast, dish):
    b_r = beast.replace(" ", "")
    d_r = dish.replace(" ", "")
    if b_r[0] == d_r[0] and b_r[-1] == d_r[-1]:
        return True
    return False
