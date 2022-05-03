// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  const dp = [[A[0], 2]];

  for (let i = 1; i < A.length; i++) {
    const day = A[i];

    const oneDay = dp[dp.length - 1][1] + 2;
    
    if (day - dp[0][0] < 7) {
      var sevenDay = 7;
    } else {
      let rewindIdx = i - 1;
      while (day - dp[rewindIdx][0] < 7) {
        rewindIdx--;
      }
      var sevenDay = dp[rewindIdx][1] + 7;
    }
    
    if (day - dp[0][0] < 30) {
      var thirtyDay = 25;
    } else {
      let rewindIdx = i - 1;
      while (day - dp[rewindIdx][0] < 30) {
        rewindIdx--;
      }
      var thirtyDay = dp[rewindIdx][1] + 25;
    }

    dp.push([day, Math.min(oneDay, sevenDay, thirtyDay)])
  }

  console.log(dp)

  return dp[dp.length - 1][1];
}

console.log(solution([1, 2, 4, 5, 7, 29, 30]))
console.log(solution([5, 7, 8, 9, 10, 12, 13]))
console.log(solution([3, 6, 8, 10, 15, 18, 19, 28]))