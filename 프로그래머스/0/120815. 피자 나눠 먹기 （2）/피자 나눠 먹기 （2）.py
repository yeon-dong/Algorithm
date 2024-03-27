def solution(n):
    i = 1
    if n % 6 == 0:
        return n // 6
    while(i*6) % n != 0:
        i+=1
    return i