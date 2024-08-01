def sum_array(arr):
    if arr == None or len(arr) < 3 or arr == []:
        return 0
    return sum(arr)-(max(arr)+min(arr))
