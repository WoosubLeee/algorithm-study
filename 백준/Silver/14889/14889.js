const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

let N;
let scores = [];
rl.on('line', line => {
  if (!N) {
    N = parseInt(line);
  } else {
    scores.push(line.split(' ').map(num => parseInt(num)));
    if (scores.length == N) rl.close();
  }
}).on('close', () => {
  const teamLength = parseInt((N+1)/2);
  let start = Array(N).fill(true);
  let link = Array(N).fill(false);
  
  let total = scores.reduce((total, line) => {
    const lineTotal = line.reduce((lineTotal, score) => lineTotal + score);
    return total + lineTotal;
  }, 0);
  
  for (let i = 0; i < N; i++) {
    for (let j = i+1; j < N; j++) {
      scores[i][j] += scores[j][i];
      scores[j][i] = scores[i][j];
    };
  };
  let minDiff = 10000000;
  
  const makeTeam = (len, idx, startScore, linkScore) => {
    if (len === teamLength) {
      if (Math.abs(startScore - linkScore) < minDiff) {
        minDiff = Math.abs(startScore - linkScore);
      }
    } else {
      let newStart, newLink;
      for (let i = idx; i < N-(teamLength-len)+1; i++) {
        newStart = startScore;
        newLink = linkScore;

        start[i] = false;
        for (let j = 0; j < N; j++) {
          if (start[j]) {
            newStart -= scores[i][j];
          } else {
            newLink += scores[i][j];
          }
        }
        link[i] = true;

        if (newLink - newStart <= minDiff) {
          makeTeam(len+1, i+1, newStart, newLink);
        }

        start[i] = true;
        link[i] = false;
      }
    }
  }

  makeTeam(0, 0, total, 0);
  console.log(minDiff);
});