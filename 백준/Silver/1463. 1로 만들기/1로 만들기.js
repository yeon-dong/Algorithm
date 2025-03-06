let N = require("fs").readFileSync(0).toString().trim();
N = Number(N);

const DP = new Array(N + 1).fill(0);

for (let i = 2; i <= N; i++) {
   
    DP[i] = DP[i - 1] + 1;

    if (i % 2 === 0) {
      DP[i] = Math.min(DP[i], DP[i / 2] + 1);
    }

    if (i % 3 === 0) {
      DP[i] = Math.min(DP[i], DP[i / 3] + 1);	
    }
}

console.log(DP[N]);