const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const N = input[0];
const que = [];
const result = [];

for(let i = 1; i <= N; i++){
  const order = input[i].trim().split(" ");
  switch (order[0]) {
    case "push":
      que.push(order[1]);
      break;
    case "pop":
      if(que.length == 0){
        result.push(-1);
      }else{
        result.push(que.shift());
      }
      break;
    case "size":
      result.push(que.length);
      break;
    case "empty":
      if(que.length == 0){
        result.push(1);
      }else{
        result.push(0);
      }
      break;
    case "front":
      if(que.length == 0){
        result.push(-1);
      }else{
        result.push(que[0]);
      }
      break;
    case "back":
      if(que.length == 0){
        result.push(-1);
      }else{
        result.push(que[que.length-1])
      }
      break;
  
    default:
      break;
  }
}

console.log(result.join("\n"));