n = int(input())
num_list = input().split(' ')
x = int(input())
num_list = [int(i) for i in num_list]
num_list = sorted(num_list)

start = 0
end = len(num_list) - 1
count = 0

while start < end:
    if(num_list[start] + num_list[end] == x):
        count += 1
    if (num_list[start] + num_list[end] <= x):
        start += 1
    else:
        end -= 1
print(count)