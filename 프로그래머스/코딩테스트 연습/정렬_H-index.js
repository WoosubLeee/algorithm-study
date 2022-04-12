function solution(citations) {
  citations.sort((a, b) => b - a);

  let answer = 0;
  for (let i = 0; i < citations.length; i++) {
    if (citations[i] >= i + 1) {
      answer = i + 1;
    } else if (citations[i] < i + 1) {
      break;
    }
  }
  return answer;
}

console.log(solution([1]));