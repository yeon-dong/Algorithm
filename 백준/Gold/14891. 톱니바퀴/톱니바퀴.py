from collections import deque

cycle1 = deque(list(map(int,input())))
cycle2 = deque(list(map(int,input())))
cycle3 = deque(list(map(int,input())))
cycle4 = deque(list(map(int,input())))
K = int(input())

def spin_cycle(cycle, move):
    if move == 1:  # 시계방향
        space = cycle.pop()
        cycle.appendleft(space)
    else:
        space = cycle.popleft()
        cycle.append(space)
    return cycle

def check_cycle():
    check = []
    if cycle1[2] != cycle2[6]:
        check.append(1)
    else:
        check.append(0)
    if cycle2[2] != cycle3[6]:
        check.append(1)
    else:
        check.append(0)
    if cycle3[2] != cycle4[6]:
        check.append(1)
    else:
        check.append(0)
    return check

for i in range(K):
    cycle_num, move = map(int, input().split())
    check = check_cycle()
    if cycle_num == 1 : # 1번 톱니
        if check[0]:
            cycle2 = spin_cycle(cycle2, -move)
            if check[1]:
                cycle3 = spin_cycle(cycle3, move)
                if check[2]:
                    cycle4 = spin_cycle(cycle4, -move)
        cycle1 = spin_cycle(cycle1, move)

    elif cycle_num == 2 : # 2번 톱니
        if check[0]:
            cycle1 = spin_cycle(cycle1, -move)
        if check[1]:
            cycle3 = spin_cycle(cycle3, -move)
            if check[2]:
                cycle4 = spin_cycle(cycle4, move)
        cycle2 = spin_cycle(cycle2, move)

    elif cycle_num == 3:  # 3번 톱니
        if check[1]:
            cycle2 = spin_cycle(cycle2, -move)
            if check[0]:
                cycle1 = spin_cycle(cycle1, move)
        if check[2]:
            cycle4 = spin_cycle(cycle4, -move)
        cycle3 = spin_cycle(cycle3, move)

    elif cycle_num == 4:  # 4번 톱니
        if check[2]:
            cycle3 = spin_cycle(cycle3, -move)
            if check[1]:
                cycle2 = spin_cycle(cycle2, move)
                if check[0]:
                    cycle1 = spin_cycle(cycle1, -move)
        cycle4 = spin_cycle(cycle4, move)

answer = 0
if cycle1[0] == 1:
    answer += 1
if cycle2[0] == 1:
    answer += 2
if cycle3[0] == 1:
    answer += 4
if cycle4[0] == 1:
    answer += 8
print(answer)