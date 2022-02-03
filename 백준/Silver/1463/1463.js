const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

rl.on('line', line => {
  const calc = () => {
    let newQueue;

    while (true) {
      newQueue = [];
      for (const num of queue) {
        if (num === 1) {
          return;
        }
        if (num % 3 === 0 && !visited.has(parseInt(num / 3))) {
          newQueue.push(parseInt(num / 3));
        }
        if (num % 2 === 0 && !visited.has(parseInt(num / 2))) {
          newQueue.push(parseInt(num / 2));
        }
        if (!visited.has(num - 1)) {
          newQueue.push(num - 1);
        }
      }
      queue = newQueue;
      count++;
    }
  }

  const N = parseInt(line);
  
  let queue = [N];
  let visited = new Set();
  let count = 0;
  
  calc();
  console.log(count);
});