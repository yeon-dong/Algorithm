def solution(todo_list, finished):
    answer=[]
    for i,j in enumerate(finished):
        if not j:
            answer.append(todo_list[i])
    return answer