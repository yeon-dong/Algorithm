def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0: #progresses 배열이 0이 될때까지 진행
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1 # 100 이상이면 빼고 count 1 증가
        else:
            if count > 0: # count가 있으면 빼고 0으로 만듦
                answer.append(count)
                count = 0
            time += 1 # time 1 증가
    answer.append(count)
    return answer