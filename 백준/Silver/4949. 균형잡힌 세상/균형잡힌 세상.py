from collections import deque
while True:
    check_string = input()
    que = deque()

    if check_string == ".":
        break

    for i in check_string:
        if i == "(" or i == "[":
            que.append(i)
        elif i == ")":
            if not que:
                que.append("false")
                break
            check = que.pop()
            if check != "(":
                que.append("false")
                break
        elif i == "]":
            if not que:
                que.append("false")
                break
            check = que.pop()
            if check != "[":
                que.append("false")
                break
    if not que:
        print("yes")
    else:
        print("no")