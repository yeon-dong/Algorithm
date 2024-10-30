n = input().split()
n = [ int(i) for i in n]
if n[0] == 1:
    msg = "ascending"
    for i in range(1,7):
        if n[i] == i+1:
            continue
        else:
            msg = "mixed"
            break
    print(msg)
elif n[0] == 8:
    j = 1
    msg = "descending"
    for i in range(7,0,-1):
        if n[j] == i:
            j += 1
            continue
        else:
            msg = "mixed"
            break
    print(msg)
else:
    print("mixed")