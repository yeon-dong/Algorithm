def solution(my_string, queries):
    for i in queries:
        answer=''
        a=list(my_string[i[0]:i[1]+1])
        a.reverse()
        answer = my_string[:i[0]]
        for j in a:
            answer += j
        answer += my_string[i[1]+1:]
        my_string = answer
    return my_string