n = int(input())
t_shirt = input().split()
t_shirt = [ int(i) for i in t_shirt]
t, p = map(int,input().split())
answer=[]
t_shirt_count = 0
for j in t_shirt:
    if j % t != 0:
        t_shirt_count += j // t + 1
    else:
        t_shirt_count += j // t
answer.append(n//p)
answer.append(n%p)
print(t_shirt_count)
print(answer[0],answer[1])