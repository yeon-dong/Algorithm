A, B ,V = map(int,input().split(' '))
one_day_before = V - A
speed = A-B
result = 0
result = one_day_before // speed
if one_day_before % speed == 0: #나머지가 없으면 다음날 다 올라가면 됨
    print(result + 1)
else: # 나머지가 있으면 하루 더 올라가야함
    print(result + 2)