S = input()
answer = [-1 for _ in range(26)]
for i in range(26):
    for j in range(len(S)):
        if ord(S[j])-97 == i:
            if answer[i] == -1:
                answer[i] = j
for k in range(26):
    print(answer[k],end=' ')