def solution(myStr):
    answer = ''
    for i in myStr:
        if i in ['a','b','c']:
            answer += ' '
        else:
            answer += i
    return "EMPTY" if answer == [] else answer.split()