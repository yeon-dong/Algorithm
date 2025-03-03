const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const N = input[0];
const stack = [];
const result = [];

for(let i = 1; i <= N; i++){
  const order = input[i].trim().split(" ");
  if(order[0] == "push"){
    stack.push(order[1]);
  }
  else if(order[0] == "pop"){
    if(stack.length == 0){
      result.push(-1);
    }else{
      result.push(stack.pop());
    }
  }
  else if(order[0] == "size"){
    result.push(stack.length)
  }
  else if(order[0] == "empty"){
    if(stack.length == 0){
      result.push(1);
    }else{
      result.push(0);
    }
  }
  else if(order[0] == "top"){
    if(stack.length == 0){
      result.push(-1);
    }else{
      result.push(stack[stack.length-1]);
    }
  }
}

console.log(result.join("\n"));