const fs = require('fs');
const inputs = fs.readFileSync('Bronze/5086/input.txt').toString().split('\n').map(line => {
  return line.split(' ').map(num => parseInt(num));
});

for (input of inputs) {
  if (input[0] === 0 && input[1] === 0) {
    break;
  }
  if (input[1] % input[0] === 0) {
    console.log('factor');
  } else if (input[0] % input[1] === 0) {
    console.log('multiple');
  } else {
    console.log('neither');
  }
}