def solution(arr):
    a = 1
    while a < len(arr):
        a *= 2
    while a != len(arr):
        arr.append(0)
    return arr