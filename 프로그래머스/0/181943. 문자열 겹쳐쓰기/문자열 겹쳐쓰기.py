def solution(my_string, overwrite_string, s):
    answer = my_string[:s]
    num = len(my_string) - len(overwrite_string) + s
    for i in overwrite_string:
        answer = answer + i
    if num > 0:
        answer = answer + my_string[(len(overwrite_string) + s):]
    return answer