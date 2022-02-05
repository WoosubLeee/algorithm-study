const fs = require('fs');

const input = fs.readFileSync('./Gold/11054/input.txt').toString().split('\n');

const N = parseInt(input[0]);
const nums = input[1].split(' ').map(num => parseInt(num));

let ascending_max, descending_max;

let ascending = [1], descending = [1];
for (let i = 1; i < N; i++) {
  ascending_max = 0;
  descending_max = 0;
  for (let j = 0; j < i; j++) {
    if (nums[j] < nums[i] && ascending[j] > ascending_max) {
      ascending_max = ascending[j];
    }
    if (nums[N-j-1] < nums[N-i-1] && descending[i-j-1] > descending_max) {
      descending_max = descending[i-j-1];
    }
  }
  ascending.push(ascending_max + 1);
  descending.unshift(descending_max + 1);
}

const result = ascending.map((asc, i) => asc + descending[i]);
console.log(Math.max(...result) - 1);