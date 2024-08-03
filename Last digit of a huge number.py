def last_digit(lst):
    if lst == []:
        return 1
    result = 1
    for i in lst[::-1]:
        if result < 4:
            result = i**result
        else:
            result = i**(result % 4+4)
    return result % 10
