def solution(arr, flag):
    answer = []
    for i,j in enumerate(arr):
        if flag[i]:
            for _ in range(j*2):
                answer.append(j)
        else:
            for _ in range(j):
                answer.pop()
    return answer