const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('input.txt')
});

rl.on('line', line => {
  let input = line.toString().split(' ');
  let a = parseInt(input[0]);
  let b = parseInt(input[1]);

  console.log(a+b);
})

//

// const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');

// for (let i = 0; i < input.length; i++) {
//   const line = input[i].split(' ');
//   let a = parseInt(line[0]);
//   let b = parseInt(line[1]);

//   console.log(a+b);
// }