def solution(n):
    answer = 1
    for i in range(n-1,0,-1):
        if n % i == 1:
            answer = i
    return answer