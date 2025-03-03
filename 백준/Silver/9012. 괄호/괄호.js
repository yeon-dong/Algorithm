const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const N = input[0];

for(let i = 1; i <= N; i++){
  const PS = input[i].split("");
  const stack = [];
  let flag = true;
  for(j of PS){
    if(j == "("){
      stack.push(j);
    }
    else if(j == ")"){
      if(stack.length==0){
        flag = false;
        break
      }
      else{
        stack.shift();
      }
    }
  }
  if(stack.length == 0 && flag){
    console.log("YES");
  }else{
    console.log("NO");
  }
}