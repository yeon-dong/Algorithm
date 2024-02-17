def solution(arr, query):
    j=0
    for i in query:
        if j % 2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
        j+=1
    return arr