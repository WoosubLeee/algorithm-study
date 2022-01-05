const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

const inputs = [];
let count = 0;
rl.on('line', line => {
  inputs.push(parseInt(line));
  count += 1;
  if (count == 2) {
    rl.close();
  }
}).on('close', () => {
  const M = inputs[0];
  const N = inputs[1];

  const isPrime = Array(N+1);
  isPrime.fill(true);
  isPrime[1] = false;
  let x;
  for (let n = 2; n <= N/2; n++) {
    if (isPrime[n]) {
      x = 2;
      while (x*n <= N) {
        isPrime[x*n] = false;
        x += 1;
      }
    }
  }

  let sum = 0;
  let min = N;
  for (let i = N; i >= M; i--) {
    if (isPrime[i]) {
      sum += i;
      min = i;
    }
  }
  if (sum) {
    console.log(`${sum}\n${min}`);
  } else {
    console.log(-1);
  }
})