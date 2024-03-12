def solution(str_list, ex):
    a = ''
    for i in str_list:
        if ex not in i:
            a += i
    return a