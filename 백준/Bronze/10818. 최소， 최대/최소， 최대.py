N = int(input())
arr = input().split()
num_arr = []
for i in range(N):
    num_arr.append(int(arr[i]))
num_arr.sort()
print(num_arr[0],num_arr[N-1])