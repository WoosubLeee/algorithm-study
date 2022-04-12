function solution(brown, yellow) {
  const total = brown + yellow;
  let height = 3;
  while (true) {
    if (total % height === 0) {
      const width = parseInt(total / height);
      if ((height-2)*(width-2) === yellow) {
        return [width, height];
      }
    }

    height++;
  }
}

console.log(solution(10, 2));
console.log(solution(8, 1));
console.log(solution(24, 24));