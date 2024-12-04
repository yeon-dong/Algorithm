def solution(answers):
    count = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    i = 0
    while i < len(answers):
        if first[i%5] == answers[i]:
            count[0] += 1
        if second[i%8] == answers[i]:
            count[1] += 1
        if third[i%10] == answers[i]:
            count[2] += 1
        i += 1
    answer = []
    for i in range(3):
        if max(count) == count[i]:
            answer.append(i+1)
    return answer