N = int(input())
for i in range(N):
    R,S = map(str,input().split())
    R = int(R)
    for k in range(len(S)):
        print(S[k]*R,end='')
    print()