const input = require("fs").readFileSync(0).toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);

const matrix = [];

for(let i = 1; i <= n; i++){
  matrix.push(input[i].trim().split(" ").map(Number));
}
let start_x = 0;
let start_y = 0;

for(let i = 0; i < n; i++){
  for(let j = 0; j < m; j++){
    if(matrix[i][j] == 2){
      start_x = i;
      start_y = j;
    }
  }
}

const result = Array.from(Array(n), ()=> Array(m).fill(-1));


const dx = [-1,1,0,0]; 
const dy = [0,0,-1,1]; 

function bfs(i,j){
    const queue = []; 
    queue.push([i,j]); 
    while(queue.length){
     let [y,x] = queue.shift();      
     for(let i=0; i<4; i++){
         let nx = x + dx[i]; 
         let ny = y + dy[i]; 
         if(nx <0 || ny <0 || nx >=m || ny >=n) continue; 
         if(result[ny][nx] === -1 && matrix[ny][nx] === 1){
             result[ny][nx] = result[y][x] +1; 
             queue.push([ny, nx]); 
         }
       }
     }
}

for(let i=0; i<n; i++){
    for(let j=0; j<m; j++){
        if(matrix[i][j] === 2){
            result[i][j] = 0; 
            bfs(i,j)
            break; 
        }
    }
}

for (let i = 0; i < n; i++) {
    let line = '';
    for (let j = 0; j < m; j++) {
        if (matrix[i][j] === 0) {
            line += '0 ';
        } else {
            line += `${result[i][j]} `;
        }
    }
    console.log(line.trim());
}