// https://www.codewars.com/kata/55d24f55d7dd296eb9000030
var summation = function (num) {
  return (num > 1)  ? num + summation(num - 1) : 1;
}