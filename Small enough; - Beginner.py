def small_enough(array, limit):
    c = 0
    for i in array:
        if i > limit:
            c += 1

    if c != 0:
        return False
    return True
