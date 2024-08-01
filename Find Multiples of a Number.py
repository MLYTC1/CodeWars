def find_multiples(integer, limit):
    result = []
    for i in range(integer, limit + 1):
        if i % integer == 0:
            result.append(i)
    return result
