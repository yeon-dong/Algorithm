a, b = map(int,input().split())
arr_a = []
arr_b = []
for i in range(a):
    temp = input().split()
    arr_a.append(temp)
for j in range(a):
    temp = input().split()
    arr_b.append(temp)
for i in range(a):
    for j in range(b):
        print(int(arr_a[i][j]) + int(arr_b[i][j]), end=" ")
    print()