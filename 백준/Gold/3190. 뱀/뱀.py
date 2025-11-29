from collections import deque

# 보드의 크기 N 입력 (N x N)
N = int(input())

# 사과의 개수 K 입력
K = int(input())

# 보드 생성
# 0: 빈 칸
# 1: 뱀의 몸
# 3: 사과
board = [[0 for _ in range(N)] for _ in range(N)]

# 사과 위치 입력
for _ in range(K):
    row, col = map(int, input().split())
    # 문제에서 주어지는 좌표는 1-based(1 ~ N)이므로 0-based로 바꿔서 저장
    board[row - 1][col - 1] = 3  # 사과는 3

# 방향 변환 정보 개수 L
L = int(input())

# 방향 변환 정보 (시간 X, 방향 C)
# C가 'L'이면 왼쪽으로 90도 회전, 'D'이면 오른쪽으로 90도 회전
move = []
for _ in range(L):
    X, C = input().split()
    move.append([int(X), C])

# 뱀을 표현할 deque
# 각 원소는 (행, 열) 좌표를 의미
snake = deque()
snake.append((0, 0))  # 시작 위치는 (0, 0)

board[0][0] = 1  # 시작 위치에 뱀 표시

# 현재 방향 인덱스
# 동(오른쪽), 남(아래), 서(왼쪽), 북(위) 순서
# →, ↓, ←, ↑
dx = [0, 1, 0, -1]  # 행 변화량
dy = [1, 0, -1, 0]  # 열 변화량
direction = 0       # 처음에는 오른쪽(동쪽)을 보고 있음

time = 0       # 경과 시간
move_index = 0 # 현재 처리해야할 방향 변환 정보의 인덱스

# 게임 시작
while True:
    # 1초가 지남
    time += 1

    # 현재 뱀의 머리 위치 deque의 오른쪽
    head_x, head_y = snake[-1]

    # 다음 머리 위치 계산
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    # 1) 벽에 부딪히는지 확인 (범위를 벗어나면 게임 종료)
    if not (0 <= nx < N and 0 <= ny < N):
        break

    # 2) 자신의 몸과 부딪히는지 확인
    if board[nx][ny] == 1:
        break

    # 3) 이동 처리
    # 3-1) 사과가 있는 칸으로 이동하는 경우
    if board[nx][ny] == 3:
        # 머리를 새 위치로 추가
        snake.append((nx, ny))
        # 보드에 뱀 몸 표시
        board[nx][ny] = 1
        # 꼬리는 그대로 (길이 +1)
        # -> pop 안 함
    else:
        # 3-2) 사과가 없는 칸으로 이동하는 경우 (그냥 한 칸 전진)
        # 머리를 새 위치로 추가
        snake.append((nx, ny))
        board[nx][ny] = 1

        # 꼬리를 한 칸 줄여야 함 (맨 앞의 좌표 제거)
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0  # 보드에서 꼬리 자리 비우기

    # 4) 이번 시간(time)에 방향을 바꿔야 하는지 확인
    # move 리스트에는 [X, C]가 들어 있으며,
    # "X초가 끝난 뒤에" 방향을 바꾸므로,
    # time == X 인 시점에서 방향을 바꾸면 됨.
    if move_index < L and move[move_index][0] == time:
        _, C = move[move_index]

        if C == 'D':  # 오른쪽 회전
            direction = (direction + 1) % 4
        elif C == 'L':  # 왼쪽 회전
            direction = (direction - 1) % 4

        move_index += 1

# 게임이 끝난 시점의 시간 출력
print(time)
