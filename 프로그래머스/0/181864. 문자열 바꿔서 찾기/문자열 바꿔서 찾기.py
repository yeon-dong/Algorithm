def solution(myString, pat):
    new = ''
    for i in myString:
        if i == 'A':
            new += 'B'
        else:
            new += 'A'
    return 1 if pat in new else 0