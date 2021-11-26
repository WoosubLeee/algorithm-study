const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('2884/input.txt')
});

rl.on('line', line => {
  let input = line.toString().split(' ');
  let h = parseInt(input[0]);
  let m = parseInt(input[1]);

  if (m >= 45) {
    m -= 45;
  } else {
    h -= 1;
    if (h < 0) {
      h = 24 + h;
    }
    m = 15 + m;
  }
  console.log(h, m);
})

//

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split(' ');

// let h = parseInt(input[0]);
// let m = parseInt(input[1]);

// if (m >= 45) {
//   m -= 45;
// } else {
//   h -= 1;
//   if (h < 0) {
//     h = 24 + h;
//   }
//   m = 15 + m;
// }
// console.log(h, m);