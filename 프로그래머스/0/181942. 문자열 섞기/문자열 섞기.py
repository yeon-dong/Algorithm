def solution(str1, str2):
    j = 0
    answer = ''
    for i in str1:
        answer = answer + i + str2[j]
        j += 1
    return answer