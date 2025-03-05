const [N, K] = require("fs").readFileSync(0).toString().trim().split(" ").map(Number);

const que = [[N,0]];
const visited = Array(100001).fill(false);

while (que.length !== 0){
  const [now, time] = que.shift();
  
  visited[now] = true; // 방문 처리
  
  if(now === K){ // 같으면 출력
    console.log(time);
    break;
  }
  for (next of [now - 1, now + 1, now * 2]) {
    if (!visited[next] && next >= 0 && next <= 100000) {
      visited[next] = 1;
      que.push([next, time + 1]);
    }
  }
}