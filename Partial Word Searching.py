def word_search(query, seq):
    c = []
    for i in seq:
        if query.lower() in i.lower():
            c.append(i)
    if len(c) == 0:
        return ['None']
    else:
        return c
