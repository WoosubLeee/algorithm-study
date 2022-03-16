const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
});

let N;
rl.on('line', line => {
  if (!N) N = parseInt(line);
  else {
    const nums = line.split(' ').map(num => parseInt(num));

    const list = [nums[0]];
    for (num of nums.slice(1)) {
      if (num < list[0]) {
        list[0] = num;
      } else if (num > list[list.length - 1]) {
        list.push(num);
      } else {
        let left = 0, right = list.length - 1;

        while (left <= right) {
          const mid = parseInt((left + right) / 2);

          if (list[mid] < num) {
            left = mid + 1;
          } else {
            right = mid - 1;
          }
        }

        list[left] = num;
      }
    }

    console.log(list.length);
  }
});