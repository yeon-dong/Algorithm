a = input()
b = input().split()
v = input()
count = 0
for i in range(len(b)):
    if(v==b[i]):
        count += 1
print(count)