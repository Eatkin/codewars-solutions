// https://www.codewars.com/kata/515e271a311df0350d00000f
function squareSum(numbers){
  sum = 0;
  numbers.forEach(function(num) {
    sum += num ** 2
  });
  return sum;
}