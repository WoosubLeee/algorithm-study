const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('input.txt')
});

let mul = 1;
let count = 0;
rl.on('line', line => {
  count += 1;
  let num = parseInt(line);
  mul *= num;

  if (count == 3) {
    rl.close();
  }
}).on('close', () => {
  const counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  while (mul > 0) {
    counts[mul % 10] += 1;
    mul = parseInt(mul / 10);
  }
  
  for (let i = 0; i < 10; i++) {
    console.log(counts[i]);
  }
});