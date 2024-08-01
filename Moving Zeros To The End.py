# 1 solution
def move_zeros(lst):
    r = [ele for ele in lst if ele != 0]
    s = [ele for ele in lst if ele == 0]
    return r+s

# 2 solution
def move_zeros(lst):
    non_zeros = [r for r in lst if r != 0]
    zeros = [r for r in lst if r == 0]
    return non_zeros + zeros

# 3 solution

def move_zeros(lst):
    r = [ele for ele in lst if ele != 0]
    s = [ele for ele in lst if ele == 0]
    return r+s
