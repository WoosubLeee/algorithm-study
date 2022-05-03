function solution(T) {
  let counts = {};
  for (let tower of T) {
    addTower(new Set([tower, [tower[1], tower[0], tower[2]].join(''), [tower[0], tower[2], tower[1]].join('')]), counts);
  }
  return Math.max(...Object.values(counts));
}

function addTower(towers, counts) {
  let included = [];
  for (let tower of towers) {
    if (!(tower in counts)) {
      counts[tower] = 0;
    }
    counts[tower]++;
  }
}

console.log(solution(["aab", "cab", "baa", "baa"]))
console.log(solution(["zzz", "zbz", "zbz", "dgf"]))
console.log(solution(["abc", "cba", "cab", "bac", "bca"]))