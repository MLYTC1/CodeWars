def solve(s):
    low_c = 0
    up_c = 0
    num_c = 0
    sp_c = 0
    numbers = '1234567890'
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    for i in s:
        if i in numbers:
            num_c += 1
        elif i.lower() in letters and i == i.lower():
            low_c += 1
        elif i.lower() in letters and i != i.lower():
            up_c += 1
        else:
            sp_c += 1
    return [up_c, low_c,num_c,sp_c]