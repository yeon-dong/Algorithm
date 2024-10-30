a = int(input())
for _ in range(a):
    h,w,n = map(int,input().split())
    floor = 1
    room = 1
    for _ in range(n-1):
        if floor + 1 <= h:
            floor += 1
        else:
            room += 1
            floor = 1
    if room < 10:
        room = '0' + str(room)
    else:
        room = str(room)
    print(str(floor)+ room)