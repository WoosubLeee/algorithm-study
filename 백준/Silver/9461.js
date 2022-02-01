const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

let P = [0, 1, 1, 1, 2];
let last;
for (let i = P.length; i <= 100; i++) {
  last = P.length - 1;
  P.push(P[last] + P[last-4]);
}

let T;
let n = 0;

rl.on('line', line => {
  if (!T) T = parseInt(line);
  else {
    console.log(P[parseInt(line)]);
    n += 1;
  }
});