def solution(myString):
    answer=''
    myString = myString.lower()
    for i in range(len(myString)):
        if myString[i] == 'a':
            answer += 'A'
        else:
            answer += myString[i].lower()
    return answer