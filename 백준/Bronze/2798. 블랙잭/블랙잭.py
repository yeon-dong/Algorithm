import sys

n, m = map(int, input().split())
card_list = list(map(int,input().split()))
card_list.sort()
result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card_list[i] + card_list[j] + card_list[k] > m:
                continue
            else:
                result = max(result, card_list[i] + card_list[j] + card_list[k])
print(result)