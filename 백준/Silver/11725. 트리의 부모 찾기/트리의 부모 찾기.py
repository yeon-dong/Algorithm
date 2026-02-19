import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가 (노드 최대 100,000 대비)

N = int(sys.stdin.readline())  # 노드 개수 입력

tree = [[] for _ in range(N + 1)]  # 인접 리스트 생성 (1번부터 N번까지 사용)

for _ in range(N - 1):  # 트리는 간선이 N-1개
    a, b = map(int, sys.stdin.readline().split())  # 두 노드 입력
    tree[a].append(b)  # a에 b 연결
    tree[b].append(a)  # b에 a 연결 (무방향)

parent = [0] * (N + 1)  # 각 노드의 부모 저장 배열
visited = [False] * (N + 1)  # 방문 여부 체크 배열


def dfs(cur):  # 현재 노드 cur에서 DFS 시작
    visited[cur] = True  # 현재 노드 방문 처리

    for nxt in tree[cur]:  # 현재 노드와 연결된 모든 노드 탐색
        if not visited[nxt]:  # 아직 방문하지 않았다면
            parent[nxt] = cur  # nxt의 부모는 cur
            dfs(nxt)  # nxt를 기준으로 다시 DFS 진행


dfs(1)  # 루트 1번에서 DFS 시작

for i in range(2, N + 1):  # 2번 노드부터 N번 노드까지
    print(parent[i])  # 각 노드의 부모 출력
