def solution(d, budget):
    answer = 0
    d.sort()
    while budget > 0:
        if budget - d[0] >= 0:
            answer += 1
        budget -= d[0]
        d.pop(0)
        if len(d) == 0:
            break
    return answer