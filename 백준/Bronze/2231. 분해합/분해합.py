import sys

N = int(input())

for i in range(0,N):
    M = i
    for j in str(i):
        M += int(j)
    if(M == N):
        print(i)
        break
    elif(i==N-1):
        print(0)