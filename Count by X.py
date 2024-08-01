def count_by(x, n):
    y = []
    for i in range(1, n+1):
        y.append(i)
    return [num*x for num in y]
