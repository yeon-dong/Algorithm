def solution(my_string, m, c):
    answer = ''
    a = 0
    while a < len(my_string):
        answer += my_string[c-1+a]
        a += m
    return answer