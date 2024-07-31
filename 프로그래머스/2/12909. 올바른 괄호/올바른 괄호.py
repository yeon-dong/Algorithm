def solution(s):
    stack = []
    for i in s:
        if i == '(': # '('이면 스택에 추가
            stack.append(i)
        else: #')'이면 스택이랑 비교
            if stack == []: #')'인데 스택이 비어있으면 끝
                return False
            else:
                stack.pop() # ')'인데 스택에 '('가 있는 거니까 하나 마지막에서 빼기  
    return stack == [] #마지막에 '('가 stack에 남아있으면 false