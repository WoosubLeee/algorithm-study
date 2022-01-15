const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  // input: fs.createReadStream('/dev/stdin')
  input: process.stdin
});

let N;
const infos = [];
let n = 0;
rl.on('line', line => {
  if (!N) {
    N = parseInt(line);
  } else {
    infos.push(line.toString().split(' ').map(num => parseInt(num)));
    n += 1;

    if (n == N) {
      rl.close();
    }
  }
}).on('close', () => {
  let person, place;
  for (let i = 0; i < N; i++) {
    person = infos[i];
    place = 1;
    for (let j = 0; j < N; j++) {
      if (i !== j) {
        compare = infos[j];
        if (compare[0] > person[0] && compare[1] > person[1]) {
          place += 1;
        }
      }
    }
    console.log(place);
  }
});