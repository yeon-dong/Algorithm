# 입력:
# N: 세로 길이 (행 개수)
# M: 가로 길이 (열 개수)
# x, y: 주사위의 처음 위치 (행, 열)
# K: 명령의 개수
N, M, x, y, K = map(int, input().split())

# 지도 정보 입력
# dice_map[r][c] 에는 그 칸에 적힌 숫자가 들어있음
dice_map = [0 for _ in range(N)]
for i in range(N):
    dice_map[i] = list(map(int, input().split()))

# 이동 명령들 입력 (동=1, 서=2, 북=3, 남=4)
order = list(map(int, input().split()))

# -------------------------------------------------------------------
# 주사위 표현 방법
# 주사위를 6개의 면으로 나누어 1차원 리스트로 표현
# 인덱스 의미를 우리가 약속해서 사용하면 됨
#
# 여기서는 다음과 같이 정의할 것:
# dice[0] : 윗면 (top)
# dice[1] : 아랫면 (bottom)
# dice[2] : 북쪽 면 (north)
# dice[3] : 남쪽 면 (south)
# dice[4] : 서쪽 면 (west)
# dice[5] : 동쪽 면 (east)
#
# 처음에는 모든 면에 적힌 수가 0이라고 했으므로 0으로 초기화
dice = [0, 0, 0, 0, 0, 0]

# 이동 방향 정의
# 명령 숫자(1~4)를 그대로 인덱스로 쓰기 위해 0번은 dummy로 두고 시작
# 1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽
# x는 행, y는 열이라고 생각하면,
#   동쪽(1): y + 1
#   서쪽(2): y - 1
#   북쪽(3): x - 1
#   남쪽(4): x + 1
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# -------------------------------------------------------------------
# 주사위를 굴릴 때, 각 방향별로 주사위의 면이 어떻게 바뀌는지 구현
# (현재 dice 배열을 직접 변경하는 함수들)

def roll_east():
    """
    동쪽(오른쪽)으로 굴렸을 때의 주사위 면 변화
    (현재 위치에서 y가 +1 되는 방향)
    """
    top, bottom, north, south, west, east = dice
    # 오른쪽으로 굴리면:
    # 새 윗면   = 원래 서쪽면
    # 새 서쪽면 = 원래 아랫면
    # 새 아랫면 = 원래 동쪽면
    # 새 동쪽면 = 원래 윗면
    dice[0] = west     # top
    dice[4] = bottom   # west
    dice[1] = east     # bottom
    dice[5] = top      # east
    # 북/남은 그대로
    # dice[2] = north
    # dice[3] = south

def roll_west():
    """
    서쪽(왼쪽)으로 굴렸을 때의 주사위 면 변화
    (현재 위치에서 y가 -1 되는 방향)
    """
    top, bottom, north, south, west, east = dice
    # 왼쪽으로 굴리면:
    # 새 윗면   = 원래 동쪽면
    # 새 동쪽면 = 원래 아랫면
    # 새 아랫면 = 원래 서쪽면
    # 새 서쪽면 = 원래 윗면
    dice[0] = east     # top
    dice[5] = bottom   # east
    dice[1] = west     # bottom
    dice[4] = top      # west
    # 북/남은 그대로

def roll_north():
    """
    북쪽(위쪽)으로 굴렸을 때의 주사위 면 변화
    (현재 위치에서 x가 -1 되는 방향)
    """
    top, bottom, north, south, west, east = dice
    # 북쪽으로 굴리면:
    # 새 윗면   = 원래 남쪽면
    # 새 남쪽면 = 원래 아랫면
    # 새 아랫면 = 원래 북쪽면
    # 새 북쪽면 = 원래 윗면
    dice[0] = south    # top
    dice[3] = bottom   # south
    dice[1] = north    # bottom
    dice[2] = top      # north
    # 동/서는 그대로

def roll_south():
    """
    남쪽(아래쪽)으로 굴렸을 때의 주사위 면 변화
    (현재 위치에서 x가 +1 되는 방향)
    """
    top, bottom, north, south, west, east = dice
    # 남쪽으로 굴리면:
    # 새 윗면   = 원래 북쪽면
    # 새 북쪽면 = 원래 아랫면
    # 새 아랫면 = 원래 남쪽면
    # 새 남쪽면 = 원래 윗면
    dice[0] = north    # top
    dice[2] = bottom   # north
    dice[1] = south    # bottom
    dice[3] = top      # south
    # 동/서는 그대로

# -------------------------------------------------------------------
# 명령을 하나씩 수행하면서,
# - 지도 밖으로 나가면 그 명령은 무시(continue)
# - 정상적으로 이동하면:
#   1. 주사위를 해당 방향으로 굴리고
#   2. 칸에 적힌 수와 주사위 아랫면 숫자를 규칙에 따라 교환
#   3. 주사위 윗면 숫자를 출력

for cmd in order:
    # 다음에 이동할 좌표 계산
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    # 1) 범위를 벗어났는지 확인 (지도의 바깥으로 나가는 경우)
    if not (0 <= nx < N and 0 <= ny < M):
        # 이 명령은 무시 (출력도 하지 않음)
        continue

    # 2) 실제로 주사위를 굴림 (주사위 면 재배치)
    if cmd == 1:       # 동쪽
        roll_east()
    elif cmd == 2:     # 서쪽
        roll_west()
    elif cmd == 3:     # 북쪽
        roll_north()
    elif cmd == 4:     # 남쪽
        roll_south()

    # 3) 주사위가 이동한 위치로 좌표 갱신
    x, y = nx, ny

    # 4) 지도 칸 숫자와 주사위 아랫면 숫자를 문제의 규칙대로 처리
    #   - 만약 칸에 쓰여 있는 수가 0이면:
    #       주사위의 아랫면 숫자를 칸에 복사
    #   - 0이 아닌 다른 수가 있으면:
    #       그 칸에 있는 수를 주사위의 아랫면으로 복사하고,
    #       그 칸에는 0을 채움
    if dice_map[x][y] == 0:
        # 칸이 0이면, 주사위 아랫면 숫자를 칸에 복사
        dice_map[x][y] = dice[1]
    else:
        # 칸이 0이 아니면, 그 값을 주사위 아랫면에 복사하고
        # 칸은 0으로 만든다
        dice[1] = dice_map[x][y]
        dice_map[x][y] = 0

    # 5) 현재 주사위의 윗면 숫자를 출력
    print(dice[0])
