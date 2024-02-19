def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer > n:
            return answer
        answer += i
    return answer