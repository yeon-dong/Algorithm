import sys

N = int(input())
i=2
hexagon = 1
if N == 1: # 1이면 한칸 지나니까 1을 출력
    print(1)
# i는 0부터 N과 같거나 작을때 까지
while i <= N:
    # N이 몇번째 육각형 안에 포함되는지.
    if(N < i + hexagon * 6):
        print(hexagon+1)
        break
    else: #육각형에 포함 안되면 육각형 하나 추가, i도 다음 육각형으로 보냄
        i += hexagon * 6
        hexagon += 1