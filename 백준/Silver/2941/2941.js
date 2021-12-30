const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin//fs.createReadStream('/dev/stdin')
});

rl.on('line', line => {
  // let result = 0;
  // for (let i = 0; i < line.length; i++) {
  //   console.log(line[i]);
  //   result += 1;
  //   if (line.slice(i, i+3) === 'dz=') {
  //     i += 2;
  //   } else if (['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='].includes(line.slice(i, i+2))) {
  //     i += 1;
  //   }
  // }
  // console.log(result);

  const regexes = [/c=/g, /c-/g, /dz=/g, /d-/g, /lj/g, /nj/g, /s=/g, /z=/g];
  regexes.forEach(regex => line = line.replace(regex, 'a'));
  console.log(line.length);

  rl.close();
}).on('close', () => {
  process.exit();
});