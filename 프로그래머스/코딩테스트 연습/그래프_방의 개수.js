function solution(arrows) {
  const move = {
    0: [0, 1],
    1: [1, 1],
    2: [1, 0],
    3: [1, -1],
    4: [0, -1],
    5: [-1, -1],
    6: [-1, 0],
    7: [-1, 1]
  };


  let result = 0;

  const nodes = {};
  let from = [0, 0];
  for (arrow of arrows) {
    for (let i in [0, 1]) {
      let to = [from[0] + move[arrow][0], from[1] + move[arrow][1]];
      const oppositeArrow = arrow <= 3 ? arrow + 4 : arrow - 4;
      checkIn(nodes, [from, to]);

      if (!(nodes[from[0]][from[1]]).includes(arrow)) {
        if (nodes[to[0]][to[1]].length > 0) {
          result++;
        }

        nodes[from[0]][from[1]].push(arrow);
        nodes[to[0]][to[1]].push(oppositeArrow);
      }

      from = to;
    }
  }

  return result;
}

function checkIn(nodes, node) {
  for (n of node) {
    if (!(n[0] in nodes)) {
      nodes[n[0]] = {};
    }

    if (!(n[1] in nodes[n[0]])) {
      nodes[n[0]][n[1]] = [];
    }
  }
}

console.log(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]));
console.log(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]));
console.log(solution([5, 2, 7, 1, 6, 3]));
console.log(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]));