def distinct(seq):
    c = set()
    c1 = []
    while seq:
        if seq[0] not in c:
            c.add(seq[0])
            c1.append(seq[0])
        del seq[0]
    return c1
