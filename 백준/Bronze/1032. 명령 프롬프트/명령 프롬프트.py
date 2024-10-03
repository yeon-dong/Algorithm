a = int(input())
first = input()
if a == 1:
    print(first)
else:
    for i in range(a-1):
        answer = ""
        cmd = input()
        for j in range(len(first)):
            if first[j] == cmd[j]:
                answer += cmd[j]
            else:
                answer += "?"
        first = answer
    print(answer)