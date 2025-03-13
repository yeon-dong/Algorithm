N = int(input())
arr = []
for i in range(N):
    a,b = map(int,input().split())
    arr.append([a,b])
arr.sort(key=lambda x: (x[1],x[0]))
for j in range(N):
    print(arr[j][0],arr[j][1])