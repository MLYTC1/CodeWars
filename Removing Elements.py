def remove_every_other(my_list):
    s = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            s.append(my_list[i])
    return s
