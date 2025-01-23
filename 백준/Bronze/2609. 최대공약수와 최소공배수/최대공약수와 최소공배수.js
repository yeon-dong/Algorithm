const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((ip) => ip.trim());

let [a, b] = input[0].split(" ").map(Number);

let maxDivide = 0;
let minMulti = 0;
for (let i = 1; i <= a * b; i++) {
  if (a % i == 0 && b % i == 0) {
    maxDivide = i;
  }
  if (i % a == 0 && i % b == 0) {
    minMulti = i;
    break;
  }
}

console.log(maxDivide);
console.log(minMulti);
