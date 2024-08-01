def count_positives_sum_negatives(arr):
    r1 = []
    r2 = []
    r3 = []
    for i in arr:
        if i > 0:
            r1.append(i)
        if i < 0:
            r2.append(i)

    s2 = sum([num for num in r2])
    for n in r1:
        if n != 0:
            r3.append(n)
    if arr == []:
        return []
    if len(r3) == 0 and s2 == 0:
        return [0, 0]
    return [len(r3), s2]