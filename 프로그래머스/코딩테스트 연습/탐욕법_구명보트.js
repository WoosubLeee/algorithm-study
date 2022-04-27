function solution(people, limit) {
  people.sort((a, b) => a - b);
  people.reverse();

  let answer = 0;

  let l = 0; r = people.length - 1;
  while (l <= r) {    
    if (people[l] + people[r] <= limit) {
      r--;
    }
    l++;

    answer++;
  }

  return answer;
}

console.log(solution([70, 50, 80, 50], 100));
console.log(solution([70, 80, 50], 100));
console.log(solution([50, 40, 40, 30, 20, 20], 100));
console.log(solution([40, 50, 150, 160], 200));
console.log(solution([100, 500, 500, 900, 950], 1000));
console.log(solution([70, 50, 80, 50, 90, 40], 240));
console.log(solution([160, 150, 140, 60, 50, 40], 200));