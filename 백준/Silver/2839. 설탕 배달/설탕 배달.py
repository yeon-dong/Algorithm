# from collections import deque
N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    boxCount = 0
    while N > 0:
        N -= 3 # 3을 하나 빼줌
        boxCount += 1 # 박스 개수 추가
        if N % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            boxCount += N // 5
            print(boxCount)
            break
        elif N == 1 or N == 2:  # 3kg보다 적게 남아서 나눌 수 없을 때
            print(-1)
            break
        elif N == 0:  # 3으로 나눠떨어질 때
            print(boxCount)
            break


# deque = deque()
# deque.append([0,0])
# minList = []
#
# while deque:
#     fiveBox, threeBox = map(int,deque.popleft())
#     if (fiveBox * 5) + (threeBox * 3) == N :
#         minList.append(fiveBox+threeBox)
#     if (fiveBox + 1) * 5 + threeBox * 3 <= N:
#         deque.append([fiveBox + 1, threeBox])
#     if (threeBox + 1) * 3 + fiveBox * 5 <= N:
#         deque.append([fiveBox, threeBox + 1])
#
# if minList:
#     print(min(minList))
# else:
#     print(-1)