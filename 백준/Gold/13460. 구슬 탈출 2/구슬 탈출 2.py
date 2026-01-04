from collections import deque

# =========================
# 입력 처리
# =========================
N, M = map(int, input().split())

board = []
red = None
blue = None

for i in range(N):
    row_input = input().rstrip()
    row = []
    for j in range(M):
        if row_input[j] == 'R':
            red = (i, j)
            row.append('.')  # 보드에는 구슬이 아니라 빈칸으로 저장
        elif row_input[j] == 'B':
            blue = (i, j)
            row.append('.')
        else:
            row.append(row_input[j])
    board.append(row)

# =========================
# 방향 벡터 (상, 좌, 하, 우)
# =========================
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# =========================
# 한 구슬을 특정 방향으로 "끝까지" 굴리는 함수
# =========================
def roll(y, x, direction):
    """
    (y, x)에 있는 구슬을 direction 방향으로 굴린다.
    규칙:
      - 벽('#')을 만나기 전까지 계속 이동
      - 구멍('O')에 도달하면 즉시 종료 (구멍에 빠짐)
    반환:
      ny, nx: 최종 위치
      moved: 몇 칸 이동했는지 (겹침 처리 시 누가 더 많이 이동했는지 판단용)
      in_hole: 구멍에 빠졌는지 여부
    """
    moved = 0
    while True:
        ny = y + dy[direction]
        nx = x + dx[direction]

        # 다음 칸이 벽이면 더 이상 이동 불가
        if board[ny][nx] == '#':
            return y, x, moved, False

        # 다음 칸이 구멍이면 구멍에 빠짐
        if board[ny][nx] == 'O':
            return ny, nx, moved + 1, True

        # 빈 칸이면 이동 계속
        y, x = ny, nx
        moved += 1


# =========================
# BFS 준비
# =========================
# 방문 체크: (red_y, red_x, blue_y, blue_x)
visited = set()
visited.add((red[0], red[1], blue[0], blue[1]))

q = deque()
# (red_y, red_x, blue_y, blue_x, count)
q.append((red[0], red[1], blue[0], blue[1], 0))

# =========================
# BFS 탐색
# =========================
# 문제 조건: 10번 이하로 기울여서 성공해야 함
answer = -1

while q:
    ry, rx, by, bx, count = q.popleft()

    # 이미 10번 기울였으면 더 이상 확장 불가
    if count >= 10:
        continue

    # 네 방향으로 기울여본다
    for d in range(4):
        # 1) 빨간 구슬, 파란 구슬을 각각 굴린다
        nry, nrx, r_moved, r_in_hole = roll(ry, rx, d)
        nby, nbx, b_moved, b_in_hole = roll(by, bx, d)

        # 2) 파란 구슬이 구멍에 빠지면 실패 (빨강이 같이 빠져도 실패)
        if b_in_hole:
            continue

        # 3) 빨간 구슬만 구멍에 빠지면 성공
        if r_in_hole and not b_in_hole:
            answer = count + 1
            q.clear()  # BFS 최단거리이므로 즉시 종료를 위해 큐 비움
            break

        # 4) 두 구슬이 같은 칸에 겹치는 경우 처리
        #    (규칙상 같은 칸에 존재할 수 없으므로,
        #     더 많이 움직인 구슬을 한 칸 뒤로 물린다.)
        if nry == nby and nrx == nbx:
            if r_moved > b_moved:
                # 빨강이 더 멀리 왔으면 빨강을 한 칸 뒤로
                nry -= dy[d]
                nrx -= dx[d]
            else:
                # 파랑이 더 멀리 왔으면 파랑을 한 칸 뒤로
                nby -= dy[d]
                nbx -= dx[d]

        # 5) 방문하지 않은 상태면 큐에 추가
        state = (nry, nrx, nby, nbx)
        if state not in visited:
            visited.add(state)
            q.append((nry, nrx, nby, nbx, count + 1))

print(answer)
