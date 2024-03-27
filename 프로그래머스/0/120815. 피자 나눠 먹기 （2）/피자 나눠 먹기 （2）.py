def solution(n):
    i = 1
    while(i*6) % n != 0:
        i+=1
    return i