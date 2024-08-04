def find_missing(sequence):
    return ((sequence[0] + sequence[-1]) * (len(sequence) + 1)//2) - sum(sequence)