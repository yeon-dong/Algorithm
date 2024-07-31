def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0) # 제일 앞에거 뺌
        if any(cur[1] < q[1] for q in queue): #cur우선순위가 queue의 우선순위들보다 작은지 비교, 하나라도 크면 True 
            queue.append(cur) # queue의 맨뒤에 넣음
        else: # 제일 큰 우선순위이므로 실행
            answer += 1
            if cur[0] == location: # 실행시키는 index가 location이면 끝
                return answer