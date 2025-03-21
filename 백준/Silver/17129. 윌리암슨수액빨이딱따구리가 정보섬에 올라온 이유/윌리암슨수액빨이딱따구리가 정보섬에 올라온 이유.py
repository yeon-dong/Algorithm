import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, sys.stdin.readline().split())  # 행,열
graph = [list(map(int, list(input()))) for _ in range(n)]

dq = deque()  

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            dq.append((i, j, 0))   # 딱따구리 위치, 거리
            graph[i][j] = 1        # 방문 표시, 장애물로 변경 

while dq:
    x, y, dis = dq.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:   # 방문한 경우 or 장애물
            continue
        if graph[nx][ny] in [3, 4, 5]: # 음식인 경우 그만 
            print("TAK")
            print(dis + 1)
            exit()
        dq.append((nx, ny, dis + 1))
        graph[nx][ny] = 1

print("NIE")