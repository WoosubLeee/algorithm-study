const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
})

rl.on('line', line => {
  let alphabets = Array(26);
  alphabets.fill(0);
  
  let a;
  for (let i = 0; i < line.length; i++) {
    a = line[i].toUpperCase();
    alphabets[a.charCodeAt()-65] += 1;
  }
  
  let max_val = Math.max(...alphabets);
  if (alphabets.filter(n => n === max_val).length === 1) {
    console.log(String.fromCharCode(alphabets.indexOf(max_val)+65));
  } else {
    console.log('?');
  }
  
  rl.close();
}).on('close', () => {
  process.exit();
});