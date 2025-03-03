const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const N = input.shift();
const N_array = input.shift().trim().split(" ").map(Number)
const M = input.shift();
const M_array = input.shift().split(" ").map(Number)

const N_set = new Set(N_array);

for(i of M_array){
  let flag = true;
  if(N_set.has(i)){
    console.log(1);
    flag = false;
  }
  if(flag){
    console.log(0);
  }
}
