const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('10950/input.txt')
});

let T = null;
let countT = 0;
let data = [];

rl.on('line', line => {
  if (!T) {
    T = line;
  } else {
    let input = line.toString().split(' ');
    let a = parseInt(input[0]);
    let b = parseInt(input[1]);
    
    console.log(a+b);
    
    countT += 1;
  }
  if (countT == T) {
    rl.close();
  }
}).on('close', () => {
  process.exit();
})

//

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

// for (let i = 1; i <= input[0]; i++) {
//   let numbers = input[i].split(' ');
//   a = parseInt(numbers[0]);
//   b = parseInt(numbers[1]);
//   console.log(a+b);
// }