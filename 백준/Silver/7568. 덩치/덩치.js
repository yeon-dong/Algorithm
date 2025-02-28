const [n, ...arr] = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const people = []
for(let i = 0; i < Number(n); i++){
    let person = arr[i].trim().split(" ").map(Number);
    people.push([person[0],person[1]]);
}

const rank = []

for(let i = 0; i < n; i ++){
    let counter = 1;
    for(let j = 0; j < n; j++){
        if(i !== j){ // 같으면 본인이기 때문에 제외
            if(people[i][0] < people[j][0] &&
                people[i][1] < people[j][1] // 결국 본인보다 큰 덩치가 있으면 순위는 1씩 늘어나면 되는거임
            ){
                counter++;
            }
        }
    }
    rank.push(counter);
}

console.log(rank.join(" "));