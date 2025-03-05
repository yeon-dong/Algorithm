const input = require("fs").readFileSync(0).toString().trim().split("\n");

[N, M, V] = input[0].split(" ").map(Number);
const graph = Array.from(Array(N+1), ()=> new Array(N+1).fill(0));

for(let i = 1; i <= M; i++){
  let edge = input[i].trim().split(" ").map(Number);
  graph[edge[0]][edge[1]] = 1;
  graph[edge[1]][edge[0]] = 1;
}

const DFS_visited = new Array(N+1).fill(false);
const DFS_result = [];
const BFS_visited = new Array(N+1).fill(false);
const BFS_result = [];

function DFS(v) {
  DFS_visited[v] = true; //현재 노드 방문 처리
  DFS_result.push(v);
  for(let i = 1; i <= N; i++){
    if(graph[v][i] === 1 && DFS_visited[i] === false){ //연결 되어있고, 방문 안했으면면
      DFS(i);
    }
  }
}

function BFS(v) {
  const que = [];
  BFS_visited[v] = true; //현재 노드 방문 처리
  BFS_result.push(v);
  que.push(v);
  while (que.length !== 0){
    let now = que.shift();
    for(let i = 1; i <= N; i++){
      if (graph[now][i] === 1 && BFS_visited[i] === false) {
        BFS_visited[i] = true;
        que.push(i);
        BFS_result.push(i);
      }
    }
  }
}

DFS(V);
BFS(V);

console.log(DFS_result.join(" "));
console.log(BFS_result.join(" "));