def solution(n):
    answer = ''
    while(n >= 1):
        r = n % 3
        n = n // 3
        answer += str(r)
    return int(answer, 3)