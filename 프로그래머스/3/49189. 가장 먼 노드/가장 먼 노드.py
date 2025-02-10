# def solution(n, edge):
#     from collections import deque

#     # 그래프 초기화
#     graph = [[] for _ in range(n)]
#     for i in edge:
#         i.sort()
#         graph[i[0] - 1].append(i[1] - 1)

#     # BFS 초기화
#     queue = deque()
#     visited = [False for _ in range(n)]
#     queue.append([0, 0, visited.copy()])  # 방문 배열 복사

#     max_list = []
#     last_arr = []

#     # BFS 수행
#     while queue:
#         now = queue.popleft()
#         now[2][now[0]] = True  # 현재 노드 방문 표시

#         # 리프 노드인 경우 최단 거리 기록
#         if len(graph[now[0]]) == 0 and now[0] not in last_arr:
#             last_arr.append(now[0])
#             max_list.append(now[1])

#         # 연결된 노드 탐색
#         for i in graph[now[0]]:
#             if not now[2][i]:  # 방문하지 않은 노드라면
#                 queue.append([i, now[1] + 1, now[2].copy()])  # 방문 배열 복사하여 추가

#     # 최장 거리의 노드 개수 구하기
#     max_num = max(max_list)
#     answer = sum(1 for i in max_list if i == max_num)

#     return answer
from collections import deque

def solution(n, edge):
    answer = 0
    # 연결된 노드 정보 그래프
    graph =[[] for _ in range(n+1)]
    # 각 노드의 최단거리 리스트
    distance = [-1] * (n+1)
    
    # 연결된 노드 정보 추가
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])  
    
    
    queue = deque([1]) # BFS를 위한 queue, 출발 노드 = 1
    distance[1]=0 # 출발노드의 최단거리를 0으로
    
    # BFS 수행
    while queue :
        now = queue.popleft() # 현재 노드
        
        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[now]:
            if distance[i] == -1: # 아직 방문하지 않은 노드면,
                queue.append(i) # queue에 추가
                distance[i] = distance[now] + 1 # 최단거리 갱신
    # 가장 멀리 떨어진 노드 개수 구하기
    for d in distance:
        if d == max(distance):
            answer += 1
    return answer