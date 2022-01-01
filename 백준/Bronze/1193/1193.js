const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

rl.on('line', line => {
  const X = Number(line);
  for (let i = 1;; i++) {
    if (i*(i+1)/2 >= X) {
      var num = i+1;
      var total = i*(i+1) / 2;
      break;
    }
  }
  const a = num - (total-X+1);
  const b = num - a;
  if (num % 2 == 1) {
    console.log(`${a}/${b}`);
  } else {
    console.log(`${b}/${a}`);
  }
})