def count_sheeps(sheep):
    amount = 0
    for element in sheep:
        if element == True:
            amount += 1
    return amount
