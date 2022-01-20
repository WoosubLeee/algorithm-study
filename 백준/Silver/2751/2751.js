const quickSort = (nums, left, right) => {
  if (left >= right) return;
  
  const pivotIdx = parseInt((left+right) / 2);
  const pivotNum = nums[pivotIdx];

  let l = left, r = right;

  while (l <= r) {
    while (nums[l] < pivotNum) l++;
    while (nums[r] > pivotNum) r--;

    if (l <= r) {
      [nums[l], nums[r]] = [nums[r], nums[l]];
      l++;
      r--;
    }
  }
  
  quickSort(nums, left, r);
  quickSort(nums, l, right);
}

const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  // input: fs.createReadStream('/dev/stdin')
  input: process.stdin
});

const input = [];
let N;
rl.on('line', line => {
  if (!N) N = parseInt(line);
  else {
    input.push(parseInt(line));
    if (input.length === N) rl.close();
  }
}).on('close', () => {
  const nums = input.slice(0, N+1);

  quickSort(nums, 0, N-1);
  nums.map(num => console.log(num));
})