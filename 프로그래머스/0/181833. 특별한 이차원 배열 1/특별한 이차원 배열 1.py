def solution(n):
    answer = []
    for i in range(n):
        arr = [0 for i in range(n)]
        arr[i] = 1
        answer.append(arr)

    return answer