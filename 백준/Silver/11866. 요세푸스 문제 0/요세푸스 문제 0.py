N, K = map(int,input().split(" "))
arr = [i+1 for i in range(N)]
answer = []
count = 1
now = 0
while arr:
    if count == K:
        answer.append(arr[now])
        del(arr[now])
        N -= 1
        count = 1
    else:
        count += 1
        now += 1
        if now >= N:
            now = now % N
print("<",end="")
for j in range(len(answer)):
    if j == len(answer) - 1:
        print(str(answer[j])+">",end="")
    else:
        print(str(answer[j]) + ", ",end="")
