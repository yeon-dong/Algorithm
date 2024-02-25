def solution(myString, pat):
    idx = 0
    count = 0
    while myString.find(pat,idx) != -1:
        idx = myString.find(pat,idx) + 1
        count += 1
    return count