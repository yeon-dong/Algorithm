def solution(arr, flag):
    answer = []
    for i,j in enumerate(arr):
        if flag[i]:
            answer += [j] * (j*2)
        else:
            for _ in range(j):
                answer.pop()
    return answer