const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

rl.on('line', line => {
  const N = parseInt(line);

  let queue = [N];
  let visited = new Set();
  let count = 0;

  const calc = () => {
    let newqueue;
    
    while (true) {
      newqueue = [];
      for (const num of queue) {
        if (num === 1) {
          return;
        }

        if (num % 3 === 0 && !visited.has(parseInt(num / 3))) {
          newqueue.push(parseInt(num / 3));
          visited.add(parseInt(num / 3));
        }
        if (num % 2 === 0 && !visited.has(parseInt(num / 2))) {
          newqueue.push(parseInt(num / 2));
          visited.add(parseInt(num / 2));
        }
        if (!visited.has(num - 1)) {
          newqueue.push(num - 1);
          visited.add(num - 1);
        }
      }
      queue = newqueue;
      count++;
    }
  }

  calc();
  console.log(count);
});