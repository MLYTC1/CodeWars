def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    if a != "" and b == "":
        return a
    if b != "" and a == "":
        return b
    if a != "" and b != "":
        return str(int(a)+int(b))
