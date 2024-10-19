arr = input().split()
arr = [int(i) for i in arr]
arr.sort()
a, b, c = map(int,arr)
while(not(a == b == c == 0)):
    if c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")
    arr = input().split()
    arr = [int(i) for i in arr]
    arr.sort()
    a, b, c = map(int, arr)