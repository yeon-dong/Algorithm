const input = require("fs").readFileSync(0).toString().trim().split("\n");

const no_see_list = new Set;
const result = [];

[N, M] = input[0].trim().split(" ").map(Number);

for(let i = 1; i <= N; i++){
  no_see_list.add(input[i].trim());
}

for(let j = N + 1; j <= N+M; j++){
  const name = input[j].trim();
  if(no_see_list.has(name)){
    result.push(name);
  }
}

result.sort()
console.log(result.length);
console.log(result.join("\n"));