const fs = require('fs');
const inputs = fs.readFileSync('Gold/12865/input.txt').toString().split('\n').map(line => {
  return line.split(' ').map(num => parseInt(num));
});

const N = inputs[0][0];
const K = inputs[0][1];

// [ 무게 누적합, 가치 누적합 ]
let dp = [];
for (let i = 0; i < N+1; i++) {
  dp.push(Array(K+1).fill(0));
}

for (let i = 1; i <= N; i++) {
  let weight = inputs[i][0];
  let value = inputs[i][1];
  for (let j = 1; j <= K; j++) {
    if (j < weight) {
      dp[i][j] = dp[i-1][j];
    } else {
      dp[i][j] = Math.max(dp[i-1][j-weight] + value, dp[i-1][j]);
    }
  }
}
console.log(dp.at(-1).at(-1));