N, M = map(int, input().split(" "))
array_N = []
array_M = []
for i in range(N):
    array_N.append(int(input()))
for i in range(M):
    array_M.append(int(input()))
count = 0
now = 0
for i in range(M):
  count += 1
  now += array_M[i]
  if now >= N-1:# 판 넘어가면 종료
    break

  now += array_N[now] #현재 칸 지시사항

  if now >= N-1:# 판 넘어가면 종료
    break

print(count)