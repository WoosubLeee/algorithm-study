const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
})

rl.on('line', line => {
  console.log(line.charCodeAt(0));
  rl.close();
}).on('close', () => {
  process.exit();
});