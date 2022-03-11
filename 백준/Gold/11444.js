const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
});

rl.on('line', line => {
  const n = BigInt(line);

  const A = [[1n, 1n], [1n, 0n]];
  const mod = 1000000007n;

  const dnq = n => {
    if (n <= 1) return A;
    
    const matHalf = dnq(BigInt(n / 2n));
    let result = multiply(matHalf, matHalf);
    if (n % 2n == 1) result = multiply(result, A);

    return result;
  };

  const multiply = (matA, matB) => {
    const result = [];

    for (let i = 0; i < 2; i++) {
      const row = [];
      for (let j = 0; j < 2; j++) {
        let num = 0n;
        for (let k = 0; k < 2; k++) {
          num += matA[i][k]*matB[k][j];
        }
        row.push(num % mod);
      }
      result.push(row);
    }

    return result;
  };

  console.log(parseInt(dnq(n - 1n)[0][0]));
});