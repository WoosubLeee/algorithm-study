// 정석 로직으로 풀었으나 Node.js로는 통과한 사람 없음

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
});

let n, k;
const coins = [];
rl.on('line', line => {
  if (!n) {
    [n, k] = line.split(' ').map(num => parseInt(num));
  } else {
    coins.push(parseInt(line));
    if (coins.length == n) {
      rl.close();
    }
  }
}).on('close', () => {
  const dp = Array(k+1).fill(0);
  dp[0] = 1;

  for (let i = 0; i <= n; i++) {
    for (let j = coins[i]; j <= k; j++) {
      dp[j] += dp[j - coins[i]];
    }
  }

  console.log(dp[k]);
});