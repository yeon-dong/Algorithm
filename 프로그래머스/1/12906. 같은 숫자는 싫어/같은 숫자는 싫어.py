def solution(arr):
    answer = []
    for i,j in enumerate(arr[:-1]):
        if j != arr[i+1]:
            answer.append(j)
    answer.append(arr[-1])
    return answer