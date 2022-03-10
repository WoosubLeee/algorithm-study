const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
});

rl.on('line', line => {
  const n = BigInt(line);

  const A = [[BigInt(1), BigInt(1)], [BigInt(1), BigInt(0)]];
  const mod = BigInt(1000000007);

  const dnq = n => {
    if (n <= 1) return A;

    const matHalf = dnq(BigInt(n/BigInt(2)));
    let result = multiply(matHalf, matHalf);
    if (n % BigInt(2) == 1) result = multiply(result, dnq(1));

    return result;
  };

  const multiply = (matA, matB) => {
    const newMat = [[BigInt(0), BigInt(0)], [BigInt(0), BigInt(0)]];
 
		newMat[0][0] = ((matA[0][0] * matB[0][0]) + (matA[0][1] * matB[1][0])) % mod;
		newMat[0][1] = ((matA[0][0] * matB[0][1]) + (matA[0][1] * matB[1][1])) % mod;
		newMat[1][0] = ((matA[1][0] * matB[0][0]) + (matA[1][1] * matB[1][0])) % mod;
		newMat[1][1] = ((matA[1][0] * matB[0][1]) + (matA[1][1] * matB[1][1])) % mod;

    return newMat;
  };

  console.log(parseInt(dnq(n-BigInt(1))[0][0]));
});