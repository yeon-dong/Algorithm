const input = require("fs").readFileSync(0).toString().trim().split("\n");
const [N,K] = input[0].trim().split(" ").map(Number);
const bags = [];
for(let i = 1; i <= N; i++){
  bags.push(input[i].trim().split(" ").map(Number));
}

const dp = Array.from({ length: N + 1 }, () => Array(K + 1).fill(0));

for (let i = 1; i < N + 1; i++) {
  const [W, V] = bags[i-1]; // 현재 배낭 무게 [W]와 가치 [V]
  for (let j = 1; j <= K; j++) {
    // console.log("현재 배낭 : ",bags[i-1],j,dp);
    if (j - W >= 0) {dp[i][j] = Math.max(dp[i - 1][j - W] + V, dp[i - 1][j]);
      // console.log("비교 - dp[" ,i-1,j-W,"]+",V,"| dp[",i-1,j,"]" );
    }// 현재 열이 W 이상이면
    else dp[i][j] = dp[i - 1][j];
  }
}

console.log(dp[N][K]);