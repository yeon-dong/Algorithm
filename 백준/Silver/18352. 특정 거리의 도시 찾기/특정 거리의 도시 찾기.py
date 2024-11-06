from collections import deque
import sys
f = sys.stdin.readline

N, M, K, X = map(int,f().split())
city_map = [[] for _ in range(N)] #1234가 0123으로 바뀜
for _ in range(M):
    a, b = map(int,f().split())
    city_map[a-1].append(b-1) #1234가 0123으로 바뀜
dq = deque()
dq.append([X-1,0])
visited = [K+1 for _ in range(N)] #최단거리 넣기
while dq:
    now = dq.popleft()
    if visited[now[0]] > now[1]:  # 지금 거리가
        visited[now[0]] = now[1]
        for i in city_map[now[0]]: #지금 도시의 단방향 맵을 확인함
            dq.append([ i, now[1]+1 ])
if K in visited:
    for j in range(N):
        if visited[j] == K:
            print(j+1)
else:
    print(-1)