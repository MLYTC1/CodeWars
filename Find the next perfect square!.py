def find_next_square(sq):
    num = ((sq**0.5)+1)**2
    if num == int(num):
        return num
    return -1
