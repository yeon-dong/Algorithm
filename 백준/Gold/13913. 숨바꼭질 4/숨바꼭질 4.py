from collections import deque  # BFS에서 사용할 큐 자료구조(deque) 임포트

def solve(start, end):
    MAX = 100000  # 문제에서 좌표(수)의 범위를 보통 0~100000으로 제한하므로 최대값 설정

    visited = [-1] * (MAX + 1)   # visited[x] = start에서 x까지의 최단 거리(방문 전이면 -1)
    parent  = [-1] * (MAX + 1)   # parent[x] = x로 오기 직전의 위치(경로 복원을 위한 배열)

    q = deque([start])           # BFS 큐 초기화: 시작점 start를 큐에 넣고 시작
    visited[start] = 0           # 시작점까지의 거리는 0(이동 횟수 0)
    parent[start] = start        # 시작점의 부모는 자기 자신으로 설정(역추적 종료 조건으로 사용)

    while q:                     # 큐가 빌 때까지 반복(BFS 탐색)
        x = q.popleft()          # 큐에서 현재 위치 x를 꺼냄(가장 먼저 들어온 상태)

        if x == end:             # 도착점에 도달했다면
            break                # BFS 종료(처음 도달한 순간이 최단거리)

        # 현재 위치 x에서 갈 수 있는 다음 위치들(연산 3가지)
        for nx in (x - 1, x + 1, x * 2):
            # 다음 위치 nx가 범위 안(0~MAX)이고 아직 방문하지 않았다면
            if 0 <= nx <= MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1  # nx까지의 최단거리는 x의 최단거리 + 1
                parent[nx] = x                # nx는 x에서 왔다(부모 기록 → 경로 복원에 사용)
                q.append(nx)                  # nx를 큐에 넣어서 다음에 탐색하도록 함

    # -------- 경로 복원(역추적) --------
    path = []                   # 최종 경로를 저장할 리스트
    cur = end                   # 도착점에서부터 시작점으로 거꾸로 따라갈 변수

    while cur != parent[cur]:   # 시작점에 도달할 때까지 반복(시작점은 parent[start] = start)
        path.append(cur)        # 현재 위치 cur을 경로에 추가(현재는 end -> start 방향)
        cur = parent[cur]       # 부모(이전 위치)로 이동하며 역추적

    path.append(start)          # 반복이 끝나면 start가 아직 path에 없으므로 start 추가
    path.reverse()              # 역방향(end->start)으로 모였으니 정방향(start->end)으로 뒤집기

    return visited[end], path   # 최단 거리(이동 횟수), 실제 경로 리스트 반환

# -------- 입력 처리 및 출력 --------
start, end = map(int, input().split())  # 시작점과 도착점 입력 받기(예: 5 17)
dist, path = solve(start, end)          # BFS로 최단 거리와 경로 구하기
print(dist)                             # 최단 거리(이동 횟수) 출력
print(" ".join(map(str, path)))         # 경로를 공백으로 구분해 출력(숫자 리스트 -> 문자열 변환 필요)
