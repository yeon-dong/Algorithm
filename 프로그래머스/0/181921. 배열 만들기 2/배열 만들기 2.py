def solution(l, r):
    answer = []
    a = ['0', '5']
    for i in range(l, r+1):
        if all(num in a for num in str(i)):
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer