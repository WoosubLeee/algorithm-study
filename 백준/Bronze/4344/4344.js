const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

for (let i = 1; i <= parseInt(input[0]); i++) {
  let lineInput = input[i].split(' ');
  let scores = lineInput.slice(1).map(score => parseInt(score));
  let sum = scores.reduce((sum, score) => sum + score, 0);
  let avg = sum / scores.length;
  
  let overAvg = scores.filter(score => score > avg);
  let proportion = overAvg.length / scores.length;
  console.log((proportion*100).toFixed(3) + '%');
}