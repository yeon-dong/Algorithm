const input = require("fs").readFileSync(0).toString().trim().split("\n");

const [M, N] = input[0].trim().split(" ").map(Number);

const box_list = [];

for(let i = 1; i <= N; i++){
  box_list.push(input[i].trim().split(" ").map(Number));
}

const dx = [1,0,-1,0];
const dy = [0,1,0,-1];

const queue = [];
const dist = Array.from(Array(N),()=>Array(M).fill(0));

for (let i=0; i < N; i++) {
  for (let j=0; j < M; j++) {
      // 익은 토마토일 시 queue에 넣어 주변 익지않은 토마토 탐색
      if (box_list[i][j] === 1) {
        queue.push([i,j]);
      }
      // 익지 않은 토마토일 시
      if (box_list[i][j] === 0) {
        dist[i][j] = -1;
      }
  }
}

let head = 0;
// 익은토마토만 queue에 있음
while (queue.length > head) {
  // console.log(queue,"que");
  // console.log(dist);
  
  
    const [x,y] = queue[head++]; // 맨 앞에서 하나 shift 해줬다고 생각하면 됨
        // const [x,y] = queue.shift(); // 맨 앞에서 하나 shift 해줬다고 생각하면 됨

    for (let k=0; k<4; k++) {
        const nx = x + dx[k];
        const ny = y + dy[k];
        if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue; // 격자를 빠져나가지 않도록
        // 익은 토마토 = 0 / 빈칸(-1 인데 dist에서는 다 0)일시 넘어가기
        if (dist[nx][ny] >= 0) continue;
        // 익지않은 토마토에 대해 +1
        dist[nx][ny] = dist[x][y] + 1;
        // 주변 토마토 탐색
        queue.push([nx,ny]);
    }
}

// 토마토가 익을 때까지의 최소 날짜 출력
let day = 0;
let flag = false;
for (let i=0; i < N; i++) {
    for (let j=0; j < M; j++) {
        // 익지 않은 토마토가 있음
        if (dist[i][j] === -1){
          flag = true;
          break;
        } 
        day = Math.max(day, dist[i][j]);
    }
}

console.log(flag ? -1 : day);
