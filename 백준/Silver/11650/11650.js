const heapify = (arr, idx, size) => {
  let largest = idx;
  const leftIdx = 2*idx;
  const rightIdx = 2*idx + 1;

  if (leftIdx <= size && compare(arr, largest, leftIdx)) {
    largest = leftIdx;
  }
  if (rightIdx <= size && compare(arr, largest, rightIdx)) {
    largest = rightIdx;
  }
  if (largest !== idx) {
    [arr[idx], arr[largest]] = [arr[largest], arr[idx]];
    heapify(arr, largest, size);
  };
};

const compare = (arr, parentIdx, childIdx) => {
  return arr[parentIdx][0] > arr[childIdx][0] || (arr[parentIdx][0] === arr[childIdx][0] && arr[parentIdx][1] > arr[childIdx][1]);
};

const fs = require('fs');

const input = fs.readFileSync('Silver/11650/input.txt').toString().trim().split('\n');
const inputs = input.map(str => str.trim().split(' ').map(num => parseInt(num)));

const len = inputs.length-1;
for (let i = parseInt(len/2); i >= 1; i--) {
  heapify(inputs, i, len);
}

for (let i = len; i >= 1; i--) {
  [inputs[1], inputs[i]] = [inputs[i], inputs[1]];
  heapify(inputs, 1, i-1)
}
console.log(inputs.slice(1).reverse().map(nums => nums.join(' ')).join('\n'));