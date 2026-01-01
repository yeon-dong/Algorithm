N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북(0) 동(1) 남(2) 서(3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

clean = 0

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[r][c] == 0:
        room[r][c] = 2  # 청소 완료 표시(벽=1과 구분)
        clean += 1

    # 2. 주변 4칸 중 청소되지 않은 빈 칸(0)이 있는지 확인
    has_unclean = False
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            has_unclean = True
            break

    if has_unclean:
        # 3. 반시계 90도 회전 -> 앞칸이 0이면 전진, 최대 4번 반복
        moved = False
        for _ in range(4):
            d = (d + 3) % 4  # 왼쪽 회전
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
                r, c = nr, nc
                moved = True
                break
        if moved:
            continue
        # 4번 회전해도 못 가면 아래 후진 로직으로

    # 4. 주변에 0이 없으면 후진(방향 유지)
    br, bc = r - dr[d], c - dc[d]
    # 경계 밖은 벽으로 간주(실제 입력에선 보통 테두리가 1이라 거의 안 걸리지만 안전장치)
    if not (0 <= br < N and 0 <= bc < M) or room[br][bc] == 1:
        print(clean)
        break
    else:
        r, c = br, bc
