H,W,N,M = map(int, input().split())
import math
col = math.ceil(H/(N+1))
row = math.ceil(W/(M+1))
print(col * row)