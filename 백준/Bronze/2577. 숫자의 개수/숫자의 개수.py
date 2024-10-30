a = int(input())
b = int(input())
c = int(input())
total = a*b*c
total = str(total)
answer = [ 0 for _ in range(10) ]
for i in range(len(total)):
    for j in range(10):
        if (total[i] == str(j)):
            answer[j] += 1
for k in range(10):
    print(answer[k])