def digital_root(n):
    s = sum([int(num) for num in str(n)])
    s1 = sum([int(nums)for nums in str(s)])
    s2 = sum([int(numb)for numb in str(s1)])
    if len(str(s)) < 2:
        return s
    if len(str(s)) == 2:
        return sum([int(numb)for numb in str(s1)])
    return sum([int(x)for x in str(s2)])
