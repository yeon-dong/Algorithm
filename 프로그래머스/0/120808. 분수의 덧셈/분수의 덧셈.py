def solution(numer1, denom1, numer2, denom2):
    answer = []
    max_num = 1
    numer = numer1*denom2+numer2*denom1
    denom = denom1*denom2
    for i in range(1,max(numer,denom)+1):
        if numer % i == 0 and denom % i == 0:
            max_num = i
    answer.append(numer//max_num)
    answer.append(denom//max_num)
    return answer