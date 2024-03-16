def solution(n):
    answer = [[0 for i in range(n)] for i in range(n)]
    x = y = 0
    dir = 'right'
    for i in range(n*n):
        answer[x][y] = i+1
        if dir == 'right':
            if y+1 == n or answer[x][y+1] != 0:
                dir = 'down'
                x += 1
            else:
                y+=1
        elif dir == 'down':
            if  x+1 == n or answer[x+1][y] != 0:
                dir = 'left'
                y -= 1
            else:
                x+=1
        elif dir == 'left':
            if y-1 == n or answer[x][y-1] != 0:
                dir = 'up'
                x -=1
            else:
                y-=1
        elif dir == 'up':
            if x-1 == n or answer[x-1][y] != 0:
                dir = 'right'
                y += 1
            else:
                x-=1
    return answer