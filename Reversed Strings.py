def solution(string):
    str = ""
    for i in range(len(string)):
        str += string[-i-1]
        i -= 1
    return str
