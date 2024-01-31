def solution(n):
    answer = 0
    if n % 2:
        for i in range(1,n+1,2):
            answer += i
    else:
        for j in range(2,n+1,2):
            answer = answer + j*j
    return answer