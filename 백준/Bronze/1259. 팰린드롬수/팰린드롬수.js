const fs = require("fs");
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split("\n")
  .map((ip) => ip.trim());
let i = 0;

while (input[i] != "0") {
  let j = input[i].length;
  let answer = true;
  for (let k = 0; j / 2 > k; k++) {
    if (input[i][k] != input[i][j - 1 - k]) {
      answer = false;
      break;
    }
  }
  if (answer) {
    console.log("yes");
  } else {
    console.log("no");
  }
  i++;
}
