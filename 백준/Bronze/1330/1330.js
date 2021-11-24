const readline = require('readline');
var fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('1330/input.txt')
});

rl.on('line', line => {
  let input = line.toString().split(' ');
  let a = parseInt(input[0]);
  let b = parseInt(input[1]);
  if (a > b) {
    console.log('>');
  } else if (a < b) {
    console.log('<');
  } else {
    console.log('==')
  }
})

//

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');

// let a = parseInt(input[0]);
// let b = parseInt(input[1]);
// if (a > b) {
//   console.log('>');
// } else if (a < b) {
//   console.log('<');
// } else {
//   console.log('==')
// }