const fs = require('fs');
const inputs = fs.readFileSync('Silver/1010/input.txt').toString().split('\n');

const T = parseInt(inputs[0]);
for (let i = 1; i <= T; i++) {
  let [N, M] = inputs[i].split(' ').map(num => parseInt(num));
  if (N < parseInt(M/2)) {
    N = M-N;
  }
  let result = 1;
  for (let j = N+1; j <= M; j++) {
    result *= j;
  }
  let divide = 1;
  for (let j = 2; j <= M-N; j++) {
    divide *= j;
  }
  console.log(parseInt(result/divide));
}