const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('2438/input.txt')
});

rl.on('line', line => {
  const N = parseInt(line);

  let answer = '';
  for (let i = 1; i <= N; i++) {
    for (let j = 0; j < i; j++) {
      answer += '*';
    }
    answer += '\n';
  }
  console.log(answer);
  rl.close();
})

//

// const fs = require('fs');

// const N = parseInt(fs.readFileSync('/dev/stdin').toString());

// let answer = '';
// for (let i = 1; i <= N; i++) {
//   for (let j = 0; j < i; j++) {
//     answer += '*';
//   }
//   answer += '\n';
// }
// console.log(answer);