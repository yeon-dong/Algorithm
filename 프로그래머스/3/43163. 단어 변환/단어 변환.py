from collections import deque
def solution(begin, target, words):
    if target not in words : 
        return  0
    return BFS(begin, target, words)

def BFS(begin, target, words):
    queue = deque()
    queue.append([begin, 0]) # 시작단어와 0으로 초기화
    
    while queue:
        now, step = queue.popleft()
        
        if now == target: #target까지 가면 return후 종료
            return step
        
        #단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            for i in range(len(now)): #단어의 길이만큼 반복하여
                if now[i] != word[i]: #단어에 알파벳 한개씩 체크해서 다른거 개수 체크
                    count += 1
                    
            if count == 1: #다른 알파벳이 1개면 queue에 추가
                queue.append([word, step+1])