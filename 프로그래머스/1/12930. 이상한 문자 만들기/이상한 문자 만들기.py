def solution(s):
    count = 0
    answer = ''
    for i in s:
        if i != ' ':
            if count % 2 == 0:
                answer += i.upper()
                count += 1
            else:
                answer += i.lower()
                count += 1
        else:
            count = 0
            answer += " "
    return answer