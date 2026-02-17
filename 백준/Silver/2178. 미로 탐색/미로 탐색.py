from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que = deque()
que.append((0, 0, 1))
grid[0][0] = 0  # 시작점도 방문 처리 (중복 방지)

while que:
    y, x, count = que.popleft()

    if y == N - 1 and x == M - 1:
        print(count)
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == 1:
            grid[ny][nx] = 0      # 여기서 방문 처리!
            que.append((ny, nx, count + 1))