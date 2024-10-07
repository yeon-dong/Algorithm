arr = []
arr_all = [ i for i in range(1,31)]
for i in range(28):
    a = int(input())
    arr.append(a)
for j in arr_all:
    if j not in arr:
        print(j)