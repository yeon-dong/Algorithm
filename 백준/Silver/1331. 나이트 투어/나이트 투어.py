check = [ input() for _ in range(36) ]
board = [[0 for _ in range(6)] for _ in range(6)]
flag = True

def is_knight_move(x1, y1, x2, y2):
    return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or \
           (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)

# 시작 좌표 (0-indexed)
sx, sy = ord(check[0][0]) - 65, int(check[0][1]) - 1
board[sx][sy] = 1  # 시작 칸 방문 처리

# 첫 칸과 마지막 칸이 나이트 이동으로 연결되는지(폐순환) 먼저 확인
fsx, fsy = sx, sy
lex, ley = ord(check[-1][0]) - 65, int(check[-1][1]) - 1
if not is_knight_move(fsx, fsy, lex, ley):
    flag = False

# 각 이동이 나이트 이동인지 + 중복 방문이 없는지 검사
if flag:
    px, py = sx, sy
    for i in range(1, len(check)):
        nx, ny = ord(check[i][0]) - 65, int(check[i][1]) - 1

        # 보드 범위 체크(안전)
        if not (0 <= nx < 6 and 0 <= ny < 6):
            flag = False
            break

        # 나이트 이동인지 확인
        if not is_knight_move(px, py, nx, ny):
            flag = False
            break

        # 방문 여부 확인(중복 방문 금지)
        board[nx][ny] += 1
        if board[nx][ny] != 1:
            flag = False
            break

        px, py = nx, ny

print("Valid" if flag else "Invalid")
