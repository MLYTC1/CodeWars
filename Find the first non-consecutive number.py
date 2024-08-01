def first_non_consecutive(arr):
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]-1:
            continue
        return arr[i + 1]
    return None
