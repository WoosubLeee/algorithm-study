const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

rl.on('line', line => {
  const N = parseInt(line);

  let result = Array(N).fill('');

  const fib = (n, h) => {
    if (n == 1) {
      result[h] += '*';
    } else {
      for (let i = 0; i < n; i += n/3) {
        for (let j = 0; j < n; j += n/3) {
          if (i === n/3 && j === n/3) {
            for (let m = i; m < 2*n/3; m++) {
              result[m+h] += ' '.repeat(n/3);
            }
          } else {
            fib(n/3, h+i);
          }
        }
      }
    }
  }

  fib(N, 0);
  for (let i = 0; i < N; i++) {
    console.log(result[i]);
  }
});