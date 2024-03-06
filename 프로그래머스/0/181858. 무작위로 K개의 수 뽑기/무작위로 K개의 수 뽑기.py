def solution(arr, k):
    answer = [arr[0]]
    for i in arr:
        if i not in answer and len(answer) < k:
            answer.append(i)
    answer += [-1 for _ in range(k-len(answer))]
    return answer