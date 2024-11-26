import sys
sys.setrecursionlimit(10**6)
M,N,K = map(int,input().split())
area = [[0]*M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    area[x][y]=2 #방문표시
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<=ny < M and area[nx][ny] == 0:
            count += dfs(nx,ny)

    return count

answer =[]

for i in range(N):
    for j in range(M):
        if area[i][j] == 0:
            answer.append(dfs(i,j))
print(len(answer))
answer.sort()
for i in answer:
    print(i, end=" ")