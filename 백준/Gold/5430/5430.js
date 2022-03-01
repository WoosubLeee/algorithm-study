const fs = require('fs');

let inputs = fs.readFileSync('Gold/5430/input.txt').toString().trim().split('\n');
inputs = inputs.map(input => input.trim());

const T = parseInt(inputs[0]);
for (let i = 0; i < T; i++) {
  const order = inputs[3*i + 1].split('');
  const nums = JSON.parse(inputs[3*i+3]);
  
  let isReverse = false;
  let isError = false;
  for (o of order) {
    if (o === 'R') {
      isReverse = !isReverse;
    } else {
      if (nums.length > 0) {
        if (isReverse) {
          nums.pop();
        } else {
          nums.shift();
        }
      } else {
        isError = true;
        break;
      }
    }
  }

  if (isReverse) nums.reverse();
  if (isError) {
    console.log('error');
  } else {
    console.log(JSON.stringify(nums));
  }
}