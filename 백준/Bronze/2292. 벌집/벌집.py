import sys

N = int(input())
i = 1
hexagon = 1
# i는 0부터 N과 같거나 작을때 까지
while i < N:
    i += 6 * hexagon # 다음 박스까지 i를 키워 놓음.
    hexagon += 1 # 박스를 키워놨으니 1칸 더 가야 하는 숫자
print(hexagon)