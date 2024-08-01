def get_size(w, h, d):
    s = 2*w*h+2*w*d+2*h*d
    a = w*h*d
    return [s, a]