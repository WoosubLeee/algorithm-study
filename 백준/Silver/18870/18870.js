const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin
  // input: fs.createReadStream('/dev/stdin')
});

let N;
rl.on('line', line => {
  if (!N) {
    N = parseInt(line);
  } else {
    const inputs = line.toString().split(' ').map(num => parseInt(num));
    const merged = mergeSort([...new Set(inputs)]);

    let nums = {};
    for (let i = 0; i < merged.length; i++) {
      nums[merged[i]] = i;
    }

    console.log(inputs.map(num => nums[String(num)]).join(' '));
  }
});

const mergeSort = arr => {
  if (arr.length <= 1) {
    return arr;
  }

  const mid = parseInt(arr.length / 2);
  const lowArr = mergeSort(arr.slice(0, mid));
  const highArr = mergeSort(arr.slice(mid));

  let merged = [];
  let l = 0; h = 0;
  while (l < lowArr.length && h < highArr.length) {
    if (lowArr[l] < highArr[h]) {
      merged.push(lowArr[l]);
      l++;
    } else {
      merged.push(highArr[h]);
      h++;
    }
  }
  merged.push(...lowArr.slice(l));
  merged.push(...highArr.slice(h));
  return merged;
}