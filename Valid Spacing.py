def valid_spacing(s):
    c = 0
    for i in s:
        if i == " ":
            c += 1
        else:
            break
    for i in s[::-1]:
        if i == " ":
            c += 1
        else:
            break
    return c == 0 and s.count("  ") == 0
