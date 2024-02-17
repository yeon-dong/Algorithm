def solution(arr):
    a = []
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
    return arr[a[0]:a[-1]+1] if 2 in arr else [-1]