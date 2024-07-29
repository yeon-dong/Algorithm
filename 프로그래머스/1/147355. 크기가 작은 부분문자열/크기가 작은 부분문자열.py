def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if len(p) == 1 and int(t[i]) <= int(p):
            answer += 1
        elif int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer