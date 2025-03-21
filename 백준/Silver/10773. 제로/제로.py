from collections import deque
K = int(input())
deque = deque()
answer = 0
for i in range(K):
    now = int(input())
    if now == 0:
        answer -= deque.pop()
    else:
        deque.append(now)
        answer += now
print(answer)