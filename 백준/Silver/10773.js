const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let K;
let count = 0;

const stack = [];
rl.on('line', line => {
  if (!K) {
    K = parseInt(line);
  } else {
    const num = parseInt(line);
    if (num !== 0) {
      stack.push(num);
    } else {
      stack.pop();
    }

    count++;
    if (count == K) {
      rl.close();
    }
  }
}).on('close', () => {
  console.log(stack.reduce((sum, num) => sum + num, 0));
})