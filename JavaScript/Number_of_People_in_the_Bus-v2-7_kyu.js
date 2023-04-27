// https://www.codewars.com/kata/5648b12ce68d9daa6b000099
var number = function(busStops){
  return busStops.reduce((acc, [on, off]) => acc + on - off, 0);
}