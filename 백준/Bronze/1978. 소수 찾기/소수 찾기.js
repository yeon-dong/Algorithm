const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
const numberArray = input[1].trim().split(" ").map(Number);
let count = 0;

for(let i = 0; i<N; i++){
    if(isPrimeNumber(numberArray[i])){
        count++;
    }
}

function isPrimeNumber(x) {
    if(x == 1){
        return false;
    }
    for(let i = 2; i<Math.floor(Math.sqrt(x))+1; i++){
        if(x%i==0){
            return false;
        }
    }
    return true;
}

console.log(count)