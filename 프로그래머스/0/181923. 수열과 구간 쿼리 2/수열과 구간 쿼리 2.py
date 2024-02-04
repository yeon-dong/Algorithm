def solution(arr, queries):
    answer = []
    for i in queries:
        arr2 = arr[i[0]:i[1]+1]
        arr2.sort()
        for j in arr2:
            if j > i[2]:
                answer.append(j)
                break
            elif arr2[len(arr2)-1] == j:
                answer.append(-1)
    return answer