const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

const make = (nums, start, N, M) => {
  if (nums.length == M) {
    console.log(nums.join(' '));
  } else {
    for (let i = start; i <= N; i++) {
      nums.push(i);
      make(nums, i, N, M);
      nums.pop();
    }
  }
};

rl.on('line', line => {
  let N, M;
  [N, M] = line.split(' ').map(num => parseInt(num));
  make([], 1, N, M);
});