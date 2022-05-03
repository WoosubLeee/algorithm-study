function solution(routes) {
  routes.sort((a, b) => {
    if (a[1] < b[1]) {
      return -1;
    }
    return 1;
  });

  let cameras = [routes[0][1]];
  for (let route of routes.slice(1)) {
    if (route[0] > cameras[cameras.length - 1]) {
      cameras.push(route[1]);
    }
  }
  
  return cameras.length;
}

console.log(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
console.log(solution([[-20,-12], [-14,-5], [-18,-13], [-5,-3]]))