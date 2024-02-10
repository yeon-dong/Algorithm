def solution(a, b, c, d):
    answer = 0
    num = [a,b,c,d]
    arr = list(set(num))
    if len(arr)==1:
        answer = a*1111
    elif len(arr) == 3:
        p = max(num, key=num.count)
        tmp = [n for n in arr if n != p]
        answer = tmp[0] * tmp[1]
    elif len(arr) == 2:
        if max([num.count(n) for n in arr]) > 2:
            p = max(num, key=num.count)
            q = min(num, key=num.count)
            answer = ((10 * p) + q)**2
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))  
    else:
        answer = min(num)
    return answer