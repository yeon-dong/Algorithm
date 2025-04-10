N = int(input())
room = [int(x) for x in input().split(" ")]
B, C = map(int, input().split(" "))
answer = 0
for i in range(N):
    answer += 1
    people = room[i] - B
    if people < 0:
        continue
    if people % C == 0:
        answer += people // C
    else:
        answer += people // C + 1
print(answer)