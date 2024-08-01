def no_space(x):
    for word in x:
        for char in word:
            char = x.replace(" ", "")
            return char
