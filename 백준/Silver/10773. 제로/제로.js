const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const K = input[0];
const stack = [];

let answer = 0;
for(let i = 1; i <= K; i++){
    let now = Number(input[i]);
    if(now == 0){
        answer -= stack.pop();
    }else{
        stack.push(now);
        answer+= now;
    }
}
console.log(answer);