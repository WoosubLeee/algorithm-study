const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

rl.on('line', line => {
  const N = Number(line);
  let five = parseInt(N / 5);
  while (five >= 0) {
    if ((N - (5*five)) % 3 == 0) {
      var three = (N - (5*five)) / 3;
      break;
    } else {
      five -= 1;
    }
  }
  if (five >= 0) {
    console.log(five + three);
  } else {
    console.log(-1);
  }
})