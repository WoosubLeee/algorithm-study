const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

let T;
rl.on('line', line => {
  if (!T) {
    T = parseInt(line);
  } else {
    const [a, b] = line.split(' ').map(num => parseInt(num));
    
    let large = Math.max(a, b);
    let small = Math.min(a, b);

    while (true) {
      let temp = large % small;
      if (temp === 0) {
        break;
      }
      [large, small] = [small, temp];
    }

    console.log(a * b / small);
  }
});