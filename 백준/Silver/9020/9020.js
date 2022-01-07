const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream("/dev/stdin")
});

const isPrime = Array(10001).fill(true);
isPrime[1] = false;
let m;
for (let i = 2; i <= 100; i++) {
  if (isPrime[i]) {
    m = 2;
    while (m*i <= 10000) {
      isPrime[m*i] = false;
      m += 1;
    }
  }
}

let previousPrime;
const primeIndex = isPrime.map((tf, i) => {
  if (tf) {
    previousPrime = i;
  }
  return previousPrime;
});

let T, n, prime;
let t = 0;
rl.on("line", line => {
  if (!T) {
    T = parseInt(line);
  } else {
    n = parseInt(line);
    prime = primeIndex[n / 2];

    while (true) {
      if (isPrime[n-prime]) {
        console.log(`${prime} ${n-prime}`)
        break;
      } else {
        prime = primeIndex[prime-1];
      }
    }

    t += 1;
    if (t == T) {
      rl.close();
    }
  }
}).on("close", () => {
  process.exit();
});