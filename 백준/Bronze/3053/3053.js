const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream("/dev/stdin")
});

rl.on("line", line => {
  const num = parseInt(line);
  console.log(Math.PI * num**2);
  
  console.log(2*(num**2));
});