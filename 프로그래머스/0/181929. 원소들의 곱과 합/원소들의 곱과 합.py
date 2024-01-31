def solution(num_list):
    a=sum(num_list)**2
    b=1
    for i in num_list:
        b *= i
    return 1 if a>b else 0