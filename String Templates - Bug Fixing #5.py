def build_string(*args):
    return "I like {}! ".format(", ".join(args))[0:-1]
