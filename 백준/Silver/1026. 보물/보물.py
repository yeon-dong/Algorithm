N = int(input())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))
S = 0
for i in range(N):
    S += min(array_A) * max(array_B)
    array_A.pop(array_A.index(min(array_A)))
    array_B.pop(array_B.index(max(array_B)))
print(S)