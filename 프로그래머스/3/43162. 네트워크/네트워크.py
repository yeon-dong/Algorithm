def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)] #컴퓨터 개수만큼 false 만들기
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n,computers, com, visited):
    visited[com] = True #방문했다고 표시
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False: #연결 되어 있는 곳 다시 재귀함수로 방문
                DFS(n, computers, connect, visited) 
    