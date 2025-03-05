const input = require("fs").readFileSync(0).toString().trim().split("\n");
const N = Number(input[0].trim());
const time_list = input[1].trim().split(" ").map(Number);

time_list.sort((a,b)=>(a-b));
let result = 0;
let now = 0;
for(let i = 0; i < time_list.length; i++){
  result += time_list[i] + now;
  now += time_list[i];
}

console.log(result);