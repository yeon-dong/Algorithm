const fs = require("fs");
const input = fs.readFileSync(0).toString().split("\n");
let n = parseInt(input[0]);
hash = input[1];
let answer = 0;
alphabet = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
];
for (let i = 0; i < 5; i++) {
  answer += (alphabet.indexOf(hash[i]) + 1) * 31 ** i;
}
console.log(answer);
