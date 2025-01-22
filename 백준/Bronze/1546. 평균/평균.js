const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((ip) => ip.trim());

let sum = 0;
let num_list = [];
num_list = input[1].split(" ").map((n) => Number(n));
const max = Math.max(...num_list);

num_list.forEach((num) => {
  sum += (num / max) * 100;
});
console.log(sum / Number(input[0]));
