import math

n = int(input())
count = 0
for i in str(math.factorial(n))[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)