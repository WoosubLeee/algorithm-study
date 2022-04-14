function solution(begin, target, words) {
  const queue = [[begin, 0]];

  while (queue.length > 0) {
    const popped = queue.shift();
    for (let i in words) {
      const word = words[i];

      if (word) {
        let diffCount = 0;
        for (let j in word) {
          if (word[j] !== popped[0][j]) {
            diffCount++;
          }
        }

        if (diffCount === 1) {
          if (word === target) {
            return popped[1] + 1;
          }
          queue.push([word, popped[1]+1]);
          words[i] = '';
        }
      }
    }
  }

  return 0;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
console.log(solution("hit", "cog", 	["hot", "dot", "dog", "lot", "log"]));