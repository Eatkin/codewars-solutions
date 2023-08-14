// https://www.codewars.com/kata/5672682212c8ecf83e000050
// 2023-06-13T09:49:14.686+0000
function dblLinear(n) {
  let u = [1];
  let y = 0;
  let z = 0;

  for (let i = 0; i < n; i++) {
    let nextY = 2 * u[y] + 1;
    let nextZ = 3 * u[z] + 1;

    if (nextY <= nextZ) {
      u.push(nextY);
      y++;
      if (nextY === nextZ) {
        z++;
      }
    } else {
      u.push(nextZ);
      z++;
    }
  }

  return u[n];
}
