def abbrev_name(name):
    l = name.split()
    l_name = l[0]
    l_lastname = l[1]

    return (l_name[0]+"."+l_lastname[0]).upper()
