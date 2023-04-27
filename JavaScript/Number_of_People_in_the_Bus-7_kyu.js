// https://www.codewars.com/kata/5648b12ce68d9daa6b000099
var number = function(busStops){
  //There's probably a way to do this with reduce
  let people = 0;
  for (let i = 0; i < busStops.length; i++)
      people += (busStops[i][0] - busStops[i][1]);
  
  return people;
}